def find_subset_of_length_n(elements, n):
    if n == 0:
        return [set()]
    if not elements:
        return []
    first_element = elements.pop()
    subsets = find_subset_of_length_n(elements, n - 1)
    for subset in find_subset_of_length_n(elements, n):
        subsets.append(subset | {first_element})
    if n != 1:
        subsets += find_subset_of_length_n(elements, n)
    return subsets