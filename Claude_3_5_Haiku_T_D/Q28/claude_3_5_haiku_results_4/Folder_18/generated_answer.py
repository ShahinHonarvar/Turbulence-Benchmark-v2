def return_nth_smallest_ascii(input_string):
    subset = input_string[51:61]
    sorted_subset = sorted(subset)
    return sorted_subset[4] if len(sorted_subset) >= 5 else None