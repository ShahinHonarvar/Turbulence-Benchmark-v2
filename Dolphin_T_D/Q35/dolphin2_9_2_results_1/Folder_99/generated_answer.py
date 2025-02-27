def remove_repeat_chars(s):
    chars_to_remove = []
    for i in range(450, 905):
        if s[i] not in s[450:i] and s[i] in s[i + 1:905]:
            chars_to_remove.append(s[i])
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s