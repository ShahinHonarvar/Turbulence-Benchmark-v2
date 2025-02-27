def find_subset_of_length_n(element_set, n):
    if len(element_set) < n:
        return 0
    if n == 0:
        return 1
    element_set_copy = element_set.copy()
    element_set_copy.remove(element_set_copy.pop())
    count = find_subset_of_length_n(element_set_copy, n - 1)
    for subset in list(itertools.combinations(element_set, n - 1)):
        count += 1
        for element in subset:
            if element not in element_set:
                break
            if element_set_set.add(element):
                break
        else:
            count -= 1
    return count