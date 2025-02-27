def find_subset_of_length_n(elements):

    def subsets(elements):
        if not elements:
            yield []
        else:
            for prefix in subsets(elements[1:]):
                yield (prefix + [elements[0]])
                yield prefix
    return len(list(subsets(elements)))