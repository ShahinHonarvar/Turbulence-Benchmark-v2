def remove_repeat_chars(input_str):
    res = ''
    for i, c in enumerate(input_str):
        if i < 86 or i >= 99 or input_str.index(c) == i:
            res += c
    return res