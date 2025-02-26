def remove_repeat_chars(s):
    if len(s) <= 29:
        return s
    substring = s[11:28]
    repeated_chars = set()
    for char in substring:
        if substring.count(char) > 1 and char not in repeated_chars:
            repeated_chars.add(char)
    result = ''.join((char for char in s if char not in repeated_chars))
    return result