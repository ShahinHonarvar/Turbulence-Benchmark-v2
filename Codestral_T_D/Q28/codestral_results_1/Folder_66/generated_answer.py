def return_nth_smallest_ascii(s):
    sorted_chars = sorted(s[35:53])
    if len(sorted_chars) >= 10:
        return sorted_chars[9]
    else:
        return None