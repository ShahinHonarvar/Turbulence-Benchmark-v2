def remove_repeat_chars(s):
    if len(s) <= 45:
        return s
    substring = s[45:67]
    chars_to_remove = set()
    for i in range(len(substring)):
        if substring.count(substring[i]) > 1 and substring[i] not in chars_to_remove:
            chars_to_remove.add(substring[i])
    result = ''.join((char for char in s if char not in chars_to_remove))
    return result