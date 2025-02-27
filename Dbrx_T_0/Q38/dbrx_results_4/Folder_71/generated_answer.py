def find_subset_of_length_n(elements):
    if len(elements) < 78:
        return 0
    if len(elements) == 78:
        return 1
    return sum((find_subset_of_length_n(subset) for subset in subsets_of_length(elements, 78)))

def subsets_of_length(elements, length):
    if length == 0:
        return [set()]
    if not elements:
        return []
    first_element = elements.pop()
    with_first = subsets_of_length(elements, length - 1)
    for subset in with_first:
        subset.add(first_element)
    without_first = subsets_of_length(elements, length)
    return with_first + without_first