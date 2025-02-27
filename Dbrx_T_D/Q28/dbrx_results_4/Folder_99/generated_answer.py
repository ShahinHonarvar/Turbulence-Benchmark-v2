def return_nth_smallest_ascii(s):
    chars = sorted(s[17:66])[7]
    if type(chars) == str:
        return chars
    else:
        return None