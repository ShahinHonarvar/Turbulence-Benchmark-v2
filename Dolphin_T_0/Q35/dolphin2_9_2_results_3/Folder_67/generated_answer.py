def remove_repeat_chars(s):
    chars_to_remove = []
    for i in range(44, 67):
        for j in range(i + 1, 67):
            if s[i] == s[j]:
                chars_to_remove.append(s[i])
                break
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s