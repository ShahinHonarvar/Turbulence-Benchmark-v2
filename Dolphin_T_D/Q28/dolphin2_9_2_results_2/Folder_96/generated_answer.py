def return_nth_smallest_ascii(s):
    sub_string = s[0:18]
    sorted_chars = sorted(set(sub_string), key=lambda x: ord(x))
    return sorted_chars[17]