def return_nth_smallest_ascii(s):
    chars = sorted(list(set(s[21:60])))
    chars.sort(key=lambda x: ord(x))
    return chars[10]