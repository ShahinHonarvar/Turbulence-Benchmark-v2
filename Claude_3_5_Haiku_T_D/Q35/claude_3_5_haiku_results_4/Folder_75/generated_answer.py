def remove_repeat_chars(s):
    if len(s) <= 52:
        return s
    substring = s[21:51]
    chars_to_remove = set()
    for i in range(len(substring)):
        if substring[i] in substring[i + 1:]:
            chars_to_remove.add(substring[i])
    result = ''.join((char for char in s if char not in chars_to_remove))
    return result