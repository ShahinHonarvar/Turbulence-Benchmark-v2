def return_nth_smallest_ascii(s):
    sorted_chars = sorted(s[:13], key=lambda x: ord(x))
    return sorted_chars[12]