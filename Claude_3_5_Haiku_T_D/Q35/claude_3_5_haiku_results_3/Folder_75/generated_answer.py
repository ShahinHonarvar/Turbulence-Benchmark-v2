def remove_repeat_chars(s):
    if len(s) <= 72:
        return s
    substring = s[21:51]
    chars_to_remove = set()
    for i in range(len(substring)):
        if substring.count(substring[i]) > 1 and substring[i] not in chars_to_remove:
            chars_to_remove.add(substring[i])
    result = s[:21] + ''.join((char for char in substring if char not in chars_to_remove)) + s[51:]
    return result