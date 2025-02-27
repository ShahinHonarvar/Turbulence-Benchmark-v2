def remove_repeat_chars(s):
    chars = [0] * 54
    s_list = list(s)
    for i in range(36, 54):
        if s_list[i] in chars[36:i]:
            chars[i] = 1
    for i in reversed(range(36, 54)):
        if chars[i]:
            del s_list[i]
    return ''.join(s_list)