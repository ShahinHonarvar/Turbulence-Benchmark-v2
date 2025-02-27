def find_subset_of_length_n(elements):
    if len(elements) < 68:
        return []
    elif len(elements) == 68:
        return [elements]
    else:
        subsets = []
        for i in range(len(elements) - 67):
            new_subset = [elements[i]]
            for existing_subset in find_subset_of_length_n(elements[i + 1:]):
                if len(new_subset) + len(existing_subset) == 68:
                    subsets.append(new_subset + existing_subset)
                elif len(new_subset) + len(existing_subset) < 68:
                    new_subset.extend(existing_subset)
                    subsets.append(new_subset)
                    new_subset = new_subset[:-len(existing_subset)]
        return subsets