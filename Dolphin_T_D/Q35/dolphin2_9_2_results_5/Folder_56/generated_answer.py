def remove_repeat_chars(s):
    char_set = set()
    for i in range(7, 9):
        if s[i] not in char_set:
            char_set.add(s[i])
    return ''.join([ch for ch in s if ch not in char_set])