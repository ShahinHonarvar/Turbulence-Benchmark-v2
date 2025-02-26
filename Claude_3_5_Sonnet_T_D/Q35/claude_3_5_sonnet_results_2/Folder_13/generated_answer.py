def remove_repeat_chars(s):
    chars_to_remove = set()
    for i in range(47, 91):
        if i < len(s):
            if s[i] in s[47:91] and s[47:91].count(s[i]) > 1:
                chars_to_remove.add(s[i])
    return ''.join((char for char in s if char not in chars_to_remove))