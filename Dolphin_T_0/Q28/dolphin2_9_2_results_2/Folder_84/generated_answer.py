def return_nth_smallest_ascii(s):
    sub_string = s[52:80]
    sorted_chars = sorted(sub_string, key=lambda x: ord(x))
    return sorted_chars[6]