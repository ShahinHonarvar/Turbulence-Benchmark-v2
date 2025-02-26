def remove_repeat_chars(s):
    chars_to_remove = set()
    for i in range(57, 90):
        if s[i] in s[57:90] and s[i] not in chars_to_remove:
            if s[57:90].count(s[i]) > 1:
                chars_to_remove.add(s[i])
    return ''.join((char for char in s if char not in chars_to_remove))