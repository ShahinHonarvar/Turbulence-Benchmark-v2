def return_nth_smallest_ascii(s):
    sorted_chars = sorted(s[20:81])
    if len(sorted_chars) >= 11:
        return sorted_chars[10]
    else:
        return None