def find_subset_of_length_n(elements_set, n):
    if n < 0 or (not elements_set and n > 0):
        return 0
    elif n == 0:
        return 1
    else:
        first_element = elements_set.pop()
        return find_subset_of_length_n(elements_set, n - 1) + find_subset_of_length_n(elements_set | {first_element}, n)