def find_subset_of_length_n(elements):
    if len(elements) < 20:
        return 0
    if len(elements) == 20:
        return 1 if sum((1 for _ in elements)) else 0
    return 1 + find_subset_of_length_n(elements - {elements.pop()}) if elements else 0