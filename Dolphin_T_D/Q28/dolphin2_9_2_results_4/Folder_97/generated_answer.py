def return_nth_smallest_ascii(s):
    sub_string = s[15:22]
    sorted_sub_string = sorted(sub_string, key=lambda x: ord(x))
    return sorted_sub_string[5]