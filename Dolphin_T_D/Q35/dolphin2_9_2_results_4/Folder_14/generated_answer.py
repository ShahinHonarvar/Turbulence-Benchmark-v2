def remove_repeat_chars(s):
    chars_to_remove = []
    for i in range(2, 5):
        if s.count(s[i]) > 1:
            chars_to_remove.append(s[i])
    return ''.join([c for c in s if c not in chars_to_remove])