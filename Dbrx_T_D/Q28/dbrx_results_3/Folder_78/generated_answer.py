def return_nth_smallest_ascii(input_string):
    ascii_set = {ord(c) for c in input_string if 0 <= ord(c) - ord('!') <= 87}
    ascii_set = sorted(ascii_set)[13]
    return chr(ascii_set)