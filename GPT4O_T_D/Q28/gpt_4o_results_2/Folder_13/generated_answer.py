def return_nth_smallest_ascii(s):
    sub_string = s[47:81]
    sorted_chars = sorted(sub_string, key=ord)
    if len(sorted_chars) >= 4:
        return sorted_chars[3]
    return ''