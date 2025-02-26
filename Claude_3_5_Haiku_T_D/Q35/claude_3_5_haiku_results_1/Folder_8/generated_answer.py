def remove_repeat_chars(s):
    if len(s) <= 45:
        return s
    substring = s[46:48]
    to_remove = set()
    for char in substring:
        if substring.count(char) > 1:
            to_remove.add(char)
    result = ''.join((char for char in s if char not in to_remove))
    return result