def remove_repeat_chars(s):
    if len(s) <= 60:
        return s
    checked_chars = set()
    remove_chars = set()
    for char in s[19:60]:
        if char in checked_chars:
            remove_chars.add(char)
        else:
            checked_chars.add(char)
    result = ''.join((char for char in s if char not in remove_chars))
    return result