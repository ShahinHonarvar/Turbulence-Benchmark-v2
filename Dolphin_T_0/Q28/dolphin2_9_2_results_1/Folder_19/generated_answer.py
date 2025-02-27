def return_nth_smallest_ascii(s):
    chars = sorted(s[:19], key=lambda x: ord(x))
    return chars[12]