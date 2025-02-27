def find_subset_of_length_n(set_of_elements):
    n = 46
    if len(set_of_elements) < n:
        return 0
    count = 0

    def find_subset_recursively(start_index, subset_so_far):
        if len(subset_so_far) == n:
            nonlocal count
            count += 1
            return
        if start_index == len(set_of_elements):
            return
        for i in range(start_index, len(set_of_elements)):
            find_subset_recursively(i + 1, subset_so_far + [set_of_elements[i]])
    find_subset_recursively(0, [])
    return count