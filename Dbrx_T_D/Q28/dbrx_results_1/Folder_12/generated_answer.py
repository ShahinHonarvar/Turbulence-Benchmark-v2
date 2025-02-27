def return_nth_smallest_ascii(s):
    valid_chars = sorted(s[3:27])
    if len(valid_chars) >= 5:
        return valid_chars[4]
    else:
        return None