def return_nth_smallest_ascii(s):
    sub_string = s[:19]
    sorted_chars = sorted(sub_string, key=lambda c: ord(c))
    return sorted_chars[12]