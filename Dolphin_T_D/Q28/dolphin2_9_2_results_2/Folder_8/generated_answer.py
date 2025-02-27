def return_nth_smallest_ascii(s):
    sub_string = s[60:89]
    ascii_list = [ord(c) for c in sub_string]
    ascii_list.sort()
    nth_smallest_value = ascii_list[6]
    return chr(nth_smallest_value)