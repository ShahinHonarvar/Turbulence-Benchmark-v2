def find_subset_of_length_n(element_set):
    if len(element_set) < 38:
        return []
    elif len(element_set) == 38:
        return [set(element_set)]
    else:
        subsets = []
        for i in range(len(element_set) - 37):
            remaining_set = element_set.copy()
            subset = set(element_set.pop())
            for j in range(i, len(element_set) - 1):
                remaining_set.remove(element_set[j])
                subset.add(element_set[j])
            subsets.extend(find_subset_of_length_n(remaining_set.copy()))
            subsets.append(subset.copy())
        return subsets