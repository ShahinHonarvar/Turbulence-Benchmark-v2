def return_nth_smallest_ascii(s):
    sub_string = s[:12]
    sorted_chars = sorted(sub_string)
    return sorted_chars[11]