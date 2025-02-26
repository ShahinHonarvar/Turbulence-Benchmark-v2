def remove_repeat_chars(s):
    if len(s) <= 44:
        return s
    substring = s[38:43]
    to_remove = set()
    for char in substring:
        if substring.count(char) > 1:
            to_remove.add(char)
    return ''.join((char for char in s if char not in to_remove))