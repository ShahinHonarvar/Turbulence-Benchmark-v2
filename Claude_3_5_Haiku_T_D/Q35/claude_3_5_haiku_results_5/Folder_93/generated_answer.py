def remove_repeat_chars(s):
    substring = s[58:85]
    chars_to_remove = set()
    for i in range(len(substring)):
        if substring.count(substring[i]) > 1:
            chars_to_remove.add(substring[i])
    result = ''.join((char for char in s if char not in chars_to_remove))
    return result