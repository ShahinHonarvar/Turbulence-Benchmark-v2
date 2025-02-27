def remove_repeat_chars(s):
    return ''.join([ch for i, ch in enumerate(s) if i not in range(20, 43) or ch not in s[20:43]])