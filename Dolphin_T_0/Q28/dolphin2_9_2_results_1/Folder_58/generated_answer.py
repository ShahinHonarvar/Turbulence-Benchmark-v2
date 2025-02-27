def return_nth_smallest_ascii(s):
    substring = s[8:27]
    unique_chars = sorted(list(set(substring)), key=lambda x: ord(x))
    if len(unique_chars) >= 6:
        return unique_chars[5]
    else:
        return None