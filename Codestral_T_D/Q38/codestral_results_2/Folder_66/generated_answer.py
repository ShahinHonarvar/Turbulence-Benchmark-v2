def find_subset_of_length_n(elements):

    def find_subset(elements, n, subset):
        if n == 0:
            return 1
        if len(elements) == 0:
            return 0
        count = 0
        for i in range(len(elements)):
            subset.append(elements[i])
            count += find_subset(elements[i + 1:], n - 1, subset)
            subset.pop()
        return count
    return find_subset(list(elements), 42, [])