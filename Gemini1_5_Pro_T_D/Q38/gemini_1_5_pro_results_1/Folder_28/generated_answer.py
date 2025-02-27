def find_subset_of_length_n(set_of_elements):
    n = 37
    if len(set_of_elements) < n:
        return 0
    count = 0

    def find_subset_recursively(index, subset):
        if len(subset) == n:
            nonlocal count
            count += 1
            return
        if index == len(set_of_elements):
            return
        find_subset_recursively(index + 1, subset)
        find_subset_recursively(index + 1, subset | {list(set_of_elements)[index]})
    find_subset_recursively(0, set())
    return count