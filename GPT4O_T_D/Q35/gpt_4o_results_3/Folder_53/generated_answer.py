def remove_repeat_chars(s):
    if len(s) <= 202:
        return s
    substring = s[201:202]
    unique_chars = set()
    repeated_chars = set()
    for char in substring:
        if char in unique_chars:
            repeated_chars.add(char)
        else:
            unique_chars.add(char)
    return ''.join((char for char in s if char not in repeated_chars))