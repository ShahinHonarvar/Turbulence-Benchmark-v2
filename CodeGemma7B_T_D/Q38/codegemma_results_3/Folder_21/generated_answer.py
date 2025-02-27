def find_subset_of_length_n(set):
    """
    Return total number of subsets of size n from a set.
    """

    def power_set(set):
        """
        Take a set as input and return the power set of the set.
        """
        if not set:
            yield set
            return
        for subset in power_set(set[1:]):
            yield subset
            yield (subset | set[0:1])
    count = 0
    for subset in power_set(set):
        if len(subset) == 722:
            count = count + 1
    return count