def return_nth_smallest_ascii(s):
    chars = [s[i] for i in range(13)]
    sorted_chars = sorted(chars, key=lambda x: (x, s.index(x)))
    return sorted_chars[12]