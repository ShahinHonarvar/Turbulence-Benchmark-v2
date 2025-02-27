def return_nth_smallest_ascii(s):
    chars = [s[i] for i in range(min(11, len(s)))]
    chars.sort()
    return chars[min(10, len(chars) - 1)]