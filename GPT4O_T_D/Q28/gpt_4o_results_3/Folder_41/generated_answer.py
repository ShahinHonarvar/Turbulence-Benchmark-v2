def return_nth_smallest_ascii(s):
    sub_str = s[58:86]
    unique_characters = sorted(set(sub_str))
    if len(unique_characters) >= 19:
        return unique_characters[18]
    return ''