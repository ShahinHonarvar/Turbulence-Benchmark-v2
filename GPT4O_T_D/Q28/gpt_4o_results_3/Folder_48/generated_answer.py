def return_nth_smallest_ascii(string):
    sub_string = string[37:60]
    sorted_chars = sorted(sub_string)
    return sorted_chars[5] if len(sorted_chars) >= 6 else None