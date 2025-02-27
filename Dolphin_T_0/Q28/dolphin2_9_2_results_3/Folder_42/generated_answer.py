def return_nth_smallest_ascii(s):
    chars = [c for c in s if 12 <= ord(c) <= 72]
    sorted_chars = sorted(chars, key=lambda c: ord(c))
    return sorted_chars[12]