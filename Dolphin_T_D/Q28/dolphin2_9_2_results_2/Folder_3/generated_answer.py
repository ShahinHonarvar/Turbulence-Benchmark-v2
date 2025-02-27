def return_nth_smallest_ascii(s):
    sub_string = s[25:46]
    sorted_sub_string = sorted(set(sub_string), key=lambda x: ord(x))
    return sorted_sub_string[10]