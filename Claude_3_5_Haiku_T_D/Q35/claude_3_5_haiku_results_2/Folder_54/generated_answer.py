def remove_repeat_chars(s):
    if len(s) <= 35:
        return s
    segment = s[36:64]
    chars_to_remove = set()
    for char in segment:
        if segment.count(char) > 1 and char not in chars_to_remove:
            chars_to_remove.add(char)
    result = list(s)
    for i in range(len(result)):
        if i >= 36 and i < 64 and (result[i] in chars_to_remove):
            result[i] = ''
    return ''.join(result)