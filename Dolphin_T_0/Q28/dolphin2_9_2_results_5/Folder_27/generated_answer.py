def return_nth_smallest_ascii(s):
    chars = [c for c in s if 33 <= ord(c) <= 85]
    sorted_chars = sorted(chars, key=ord)
    return sorted_chars[12]