def return_nth_smallest_ascii(s):
    sub_string = s[35:53]
    sorted_chars = sorted(sub_string)
    return sorted_chars[9] if len(sorted_chars) >= 10 else None