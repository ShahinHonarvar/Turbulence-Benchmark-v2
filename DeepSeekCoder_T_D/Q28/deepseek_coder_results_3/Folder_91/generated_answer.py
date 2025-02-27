def return_nth_smallest_ascii(s):
    chars = [s[i] for i in range(min(8, len(s)))]
    chars.sort()
    return chars[min(7, len(chars) - 1)]