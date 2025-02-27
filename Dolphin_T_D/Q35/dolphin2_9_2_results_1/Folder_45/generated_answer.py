def remove_repeat_chars(s):
    chars_to_remove = set()
    for i in range(40, 200):
        if s[i] in s[i + 1:200]:
            chars_to_remove.add(s[i])
    return ''.join([ch for ch in s if ch not in chars_to_remove])