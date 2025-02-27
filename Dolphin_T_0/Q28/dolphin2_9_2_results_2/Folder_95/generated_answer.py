def return_nth_smallest_ascii(s):
    chars = [s[i] for i in range(1, 47) if s[i].isascii()]
    chars.sort(key=lambda x: ord(x))
    return chars[12]