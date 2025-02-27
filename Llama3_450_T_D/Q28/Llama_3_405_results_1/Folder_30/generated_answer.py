def return_nth_smallest_ascii(s):
    chars = sorted([char for i, char in enumerate(s) if 50 <= i <= 76])
    return sorted(chars, key=lambda x: ord(x))[10]