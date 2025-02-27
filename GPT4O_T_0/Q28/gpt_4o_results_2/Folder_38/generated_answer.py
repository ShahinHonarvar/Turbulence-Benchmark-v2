def return_nth_smallest_ascii(s):
    if len(s) < 46:
        return None
    sub_string = s[:46]
    sorted_chars = sorted(sub_string)
    return sorted_chars[9] if len(sorted_chars) >= 10 else None