def return_nth_smallest_ascii(s):
    sub_string = s[44:70]
    if len(sub_string) < 15:
        raise ValueError('The substring does not have enough characters.')
    sorted_chars = sorted(sub_string)
    return sorted_chars[14]