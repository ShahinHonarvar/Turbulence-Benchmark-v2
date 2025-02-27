def find_subset_of_length_n(set_elements):
    if len(set_elements) < 300:
        return 0
    else:
        result = 1
        for _ in range(300):
            result *= len(set_elements)
            set_elements.pop()
        return result