def return_nth_smallest_ascii(s):
    chars = sorted([char for i, char in enumerate(s) if 44 <= i <= 69])
    return chars[14]