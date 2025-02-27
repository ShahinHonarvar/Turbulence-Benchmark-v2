def find_subset_of_length_n(set):

    def get_powerset(set, n):
        if n == 0:
            return [[]]
        output = []
        for subset in get_powerset(set, n - 1):
            output += [subset + [element] for element in set if element not in subset]
        return output
    return len(get_powerset(set, 327))