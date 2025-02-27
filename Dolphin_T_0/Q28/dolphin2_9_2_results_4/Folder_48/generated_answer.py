def return_nth_smallest_ascii(s):
    sub_string = s[37:60]
    sorted_sub_string = sorted(sub_string, key=lambda x: ord(x))
    if len(sorted_sub_string) < 6:
        return None
    return sorted_sub_string[5]