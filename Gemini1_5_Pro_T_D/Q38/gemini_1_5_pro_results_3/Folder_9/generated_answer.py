def find_subset_of_length_n(set_of_elements):
    n = 24
    if len(set_of_elements) < n:
        return 0
    count = 0

    def find_subset_recursively(current_index, selected_elements):
        nonlocal count
        if len(selected_elements) == n:
            count += 1
            return
        if current_index == len(set_of_elements):
            return
        selected_elements.append(set_of_elements[current_index])
        find_subset_recursively(current_index + 1, selected_elements)
        selected_elements.pop()
        find_subset_recursively(current_index + 1, selected_elements)
    find_subset_recursively(0, [])
    return count