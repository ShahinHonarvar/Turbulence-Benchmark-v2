def return_nth_smallest_ascii(s):
    chars = sorted([char for i, char in enumerate(s) if 12 <= i <= 55])
    return chars[16]