def return_nth_smallest_ascii(input_string):
    subset = [ord(char) for char in input_string if 52 <= ord(char) <= 79]
    sorted_subset = sorted(subset)
    return chr(sorted_subset[6]) if len(sorted_subset) >= 7 else None