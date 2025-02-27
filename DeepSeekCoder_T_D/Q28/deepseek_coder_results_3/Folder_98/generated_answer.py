def return_nth_smallest_ascii(s):
    chars = [s[i] for i in range(min(9, len(s)))]
    chars.sort()
    return chars[min(8, len(chars) - 1)]