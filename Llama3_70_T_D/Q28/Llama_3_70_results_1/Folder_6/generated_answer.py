def return_nth_smallest_ascii(s):
    chars = [s[i] for i in range(14, 55)]
    return sorted(chars, key=ord)[10]