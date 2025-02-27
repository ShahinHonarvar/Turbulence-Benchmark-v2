def return_n_smallest_chars(input_str):
    return sorted([x for _, x in sorted([(ord(c), c) for c in input_str])][:63])