def return_nth_smallest_ascii(s):
    chars = sorted([s[i] for i in range(14, 55) if s[i].isalpha()], key=lambda x: ord(x))
    return chars[10]