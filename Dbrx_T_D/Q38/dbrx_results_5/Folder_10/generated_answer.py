def find_subset_of_length_n(set_of_elements, n):
    if n < 0 or (not set_of_elements and n > 0):
        return 0
    if n == 0 or not set_of_elements:
        return 1
    first_element = set_of_elements.pop()
    count_with_first_element = find_subset_of_length_n(set_of_elements, n - 1)
    set_of_elements.add(first_element)
    count_without_first_element = find_subset_of_length_n(set_of_elements, n)
    return count_with_first_element + count_without_first_element