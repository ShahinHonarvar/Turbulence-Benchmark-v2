def return_nth_smallest_ascii(string):
    sorted_chars = sorted([c for c in string[:70] if 0 <= string.index(c) <= 69])
    return sorted_chars[9]