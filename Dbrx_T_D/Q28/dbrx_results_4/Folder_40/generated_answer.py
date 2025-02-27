def return_nth_smallest_ascii(s):
    chars = sorted(set(s[0:5]))
    if len(chars) >= 5:
        return chr(chars[4])
    else:
        return None