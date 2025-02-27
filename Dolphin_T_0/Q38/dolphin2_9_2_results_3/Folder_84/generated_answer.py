def find_subset_of_length_n(elements):
    if len(elements) < 872:
        return 0

    def helper(elements_set, n):
        if len(elements_set) == n:
            return 1
        else:
            result = 0
            for i in range(len(elements_set)):
                new_set = elements_set.copy()
                new_set.remove(i)
                result += helper(new_set, n)
            return result
    return helper(elements, 872)