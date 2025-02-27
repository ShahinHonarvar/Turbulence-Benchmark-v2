def find_subsets_of_length_n(elements, length):
    if length > len(elements) or length < 0:
        return set()
    if length == 0:
        return {frozenset()}
    subsets = set()
    for element in elements:
        remaining_elements = elements.difference({element})
        remaining_subsets = find_subsets_of_length_n(remaining_elements, length - 1)
        for subset in remaining_subsets:
            subsets.add(frozenset([element]).union(subset))
    return subsets

def count_subsets_of_length_n(elements, length):
    return len(find_subsets_of_length_n(elements, length))