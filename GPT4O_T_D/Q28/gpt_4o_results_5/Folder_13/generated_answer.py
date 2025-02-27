def return_nth_smallest_ascii(s):
    sub_s = s[47:81]
    sorted_chars = sorted(sub_s)
    return sorted_chars[3] if len(sorted_chars) >= 4 else None