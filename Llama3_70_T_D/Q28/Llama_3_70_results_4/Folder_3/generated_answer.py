def return_nth_smallest_ascii(s):
    chars = [s[i] for i in range(25, 46)]
    chars.sort(key=lambda x: x)
    return chars[10]