def remove_repeat_chars(s):
    chars_to_remove = set()
    for i in range(70, 200):
        for j in range(i + 1, 200):
            if s[i] == s[j]:
                chars_to_remove.add(s[i])
    return ''.join([c for c in s if c not in chars_to_remove])