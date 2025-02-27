def return_n_smallest_chars(input_string):
    return sorted([input_string[i] for i in sorted([ord(ch) for ch in input_string])[:70]], reverse=True)