def return_nth_smallest_ascii(s):
    chars = [ord(c) for c in s[1:67] if c in s[1:67]]
    return min(chars, key=lambda x: (chars.count(x), x))