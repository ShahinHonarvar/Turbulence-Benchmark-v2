def return_nth_smallest_ascii(s):
    chars = [c for c in s if 48 <= ord(c) <= 76]
    chars = sorted(chars, key=lambda x: ord(x))
    return chars[4]