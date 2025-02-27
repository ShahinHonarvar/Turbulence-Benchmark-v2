def remove_repeat_chars(s):
    chars_to_remove = []
    for i in range(2, 7):
        for j in range(i + 1, 7):
            if s[i] == s[j]:
                chars_to_remove.append(s[i])
                break
    new_s = ''
    for char in s:
        if char not in chars_to_remove:
            new_s += char
    return new_s