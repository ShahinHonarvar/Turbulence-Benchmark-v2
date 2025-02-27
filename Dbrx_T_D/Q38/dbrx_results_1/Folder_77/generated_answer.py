def find_subset_of_length_n(elements):
    if len(elements) < 360:
        return set()
    subsets = {frozenset(elements[:360])}
    for i in range(360, len(elements)):
        new_subsets = set()
        for subset in subsets:
            for element in {elements[i]} - subset:
                new_subsets.add(frozenset(subset | {element}))
        subsets |= new_subsets
    return subsets