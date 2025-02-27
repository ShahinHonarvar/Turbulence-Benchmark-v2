def return_nth_smallest_ascii(s):
    sub_string = s[20:81]
    sorted_chars = sorted(sub_string, key=lambda x: ord(x))
    if len(sorted_chars) < 11:
        return None
    return sorted_chars[10]