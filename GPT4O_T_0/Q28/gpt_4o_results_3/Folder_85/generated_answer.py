def return_nth_smallest_ascii(s):
    if len(s) < 87:
        return None
    sub_string = s[17:87]
    sorted_chars = sorted(sub_string)
    if len(sorted_chars) < 15:
        return None
    return sorted_chars[14]