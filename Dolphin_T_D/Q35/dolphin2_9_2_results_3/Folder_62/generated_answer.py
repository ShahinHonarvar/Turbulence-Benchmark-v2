def remove_repeat_chars(s):
    chars_to_remove = []
    for i in range(50, 92):
        for j in range(i + 1, 92):
            if s[i] == s[j] and s[i] not in chars_to_remove:
                chars_to_remove.append(s[i])
    s = ''.join([c for c in s if c not in chars_to_remove])
    return s