def find_subset_of_length_n(elements):

    def find_combinations(elements, n):
        if n == 0:
            return [[]]
        elif not elements or n > len(elements):
            return []
        else:
            partials = find_combinations(elements[1:], n - 1)
            return partials + [[elements[0]] + partial for partial in partials]
    return len(find_combinations(elements, 83))