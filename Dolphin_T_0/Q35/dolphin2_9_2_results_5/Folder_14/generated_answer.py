def remove_repeat_chars(s):
    chars_to_remove = []
    for i in range(2, 5):
        if s[i] in s[:i] and s[i] in s[i + 1:]:
            chars_to_remove.append(s[i])
    return ''.join((char for char in s if char not in chars_to_remove))