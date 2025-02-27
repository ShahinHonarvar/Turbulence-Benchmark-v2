def return_nth_smallest_ascii(s):
    chars = [s[i] for i in range(1, 67)]
    chars.sort()
    return chars[7]