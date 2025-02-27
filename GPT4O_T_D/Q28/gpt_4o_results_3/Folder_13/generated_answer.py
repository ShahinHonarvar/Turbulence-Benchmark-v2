def return_nth_smallest_ascii(s):
    if len(s) < 81:
        return None
    sub_string = s[47:81]
    sorted_chars = sorted(sub_string)
    return sorted_chars[3] if len(sorted_chars) >= 4 else None