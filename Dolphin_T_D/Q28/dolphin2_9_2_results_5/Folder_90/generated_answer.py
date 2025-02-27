def return_nth_smallest_ascii(s):
    chars = filter(lambda c: 17 <= s.index(c) <= 83, s)
    sorted_chars = sorted(chars, key=ord)
    return sorted_chars[4]