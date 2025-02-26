def remove_repeat_chars(s):
    if len(s) <= 11:
        return s
    substr = s[11:76]
    chars_to_remove = set()
    for i in range(len(substr)):
        if substr[i] in substr[i + 1:] and substr[i] not in chars_to_remove:
            chars_to_remove.add(substr[i])
    result = ''.join((char for char in s if char not in chars_to_remove))
    return result