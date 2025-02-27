def return_nth_smallest_ascii(s):
    chars = [s[i] for i in range(42, 60)]
    chars.sort(key=lambda c: ord(c))
    return chars[16]