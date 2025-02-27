def return_nth_smallest_ascii(in_str):
    nth_smallest_ASCII = min([ord(x) for i, x in enumerate(in_str) if i >= 1 and i <= 36])
    return nth_smallest_ASCII