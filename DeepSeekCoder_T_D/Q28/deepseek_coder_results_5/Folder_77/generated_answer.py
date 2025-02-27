def return_nth_smallest_ascii(s):
    chars = [s[i] for i in range(63, 77)]
    chars.sort()
    return chars[13]