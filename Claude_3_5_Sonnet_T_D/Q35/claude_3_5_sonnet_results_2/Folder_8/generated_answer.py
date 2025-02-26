def remove_repeat_chars(s):
    if len(s) <= 46:
        return s
    target_slice = s[46:48]
    repeat_chars = set([char for char in target_slice if target_slice.count(char) > 1])
    result = ''
    for char in s:
        if char not in repeat_chars:
            result += char
    return result