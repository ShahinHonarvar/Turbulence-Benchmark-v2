def return_nth_smallest_ascii(s):
    sub_string = s[3:27]
    sorted_chars = sorted(sub_string)
    return sorted_chars[4] if len(sorted_chars) >= 5 else None