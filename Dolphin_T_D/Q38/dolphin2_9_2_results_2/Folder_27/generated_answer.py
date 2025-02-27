def find_subset_of_length_n(elements):

    def find_combinations(elements, n, i=0, current=None):
        if current is None:
            current = set()
        if n == 0:
            result.append(current)
        if n > 0 and i < len(elements):
            find_combinations(elements, n - 1, i + 1, current)
            find_combinations(elements, n - 1, i + 1, current.union({elements[i]}))
    result = []
    find_combinations(elements, 56)
    return len(result)