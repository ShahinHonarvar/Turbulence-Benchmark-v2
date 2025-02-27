def find_subset_of_length_n(element_set, n):
    if n == 0:
        return [set()]
    if not element_set:
        return []
    first_element = element_set.pop()
    with_first = [{first_element}, *map(lambda s: s | {first_element}, find_subset_of_length_n(element_set, n - 1))]
    without_first = find_subset_of_length_n(element_set, n)
    return with_first + without_first

def count_subsets_of_length_n(element_set, n):
    return len(find_subset_of_length_n(element_set, n))