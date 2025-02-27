def return_nth_smallest_ascii(s):
    sub_string = s[17:35]
    sorted_sub_string = sorted(sub_string, key=lambda x: ord(x))
    return sorted_sub_string[17] if len(sorted_sub_string) >= 18 else None