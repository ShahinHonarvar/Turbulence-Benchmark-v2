def remove_repeat_chars(s):
    if len(s) <= 3:
        return s
    substring = s[3:8]
    chars_to_remove = set()
    for char in substring:
        if substring.count(char) > 1:
            chars_to_remove.add(char)
    result = ''.join((char for char in s if char not in chars_to_remove))
    return result