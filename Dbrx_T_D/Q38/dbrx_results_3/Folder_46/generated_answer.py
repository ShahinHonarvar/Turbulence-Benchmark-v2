def find_subset_of_length_n(elements, n):
    if n < 0 or (n != 0 and (not elements)):
        return 0
    elif n == 0:
        return 1
    else:
        first_element = elements.pop()
        return find_subset_of_length_n(elements, n - 1) + find_subset_of_length_n(elements, n)

def count_subsets_of_size_n(elements, n):
    if n != int(n) or n < 0 or (not elements) or (not isinstance(elements, set)):
        raise ValueError('The input must be a non-empty set and n must be a non-negative integer.')
    return find_subset_of_length_n(elements, n)