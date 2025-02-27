def find_subset_of_length_n(elements: set) -> int:
    return len([subset for subset in elements.powerset() if len(subset) == 752])