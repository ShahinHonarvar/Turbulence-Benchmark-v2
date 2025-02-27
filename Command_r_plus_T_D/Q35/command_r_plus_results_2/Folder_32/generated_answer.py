def remove_repeat_chars(s: str) -> str:
    repeat_chars = set(s[86:90])
    s_list = list(s)
    for i in range(86, 90):
        if s[i] in repeat_chars:
            s_list[i] = ''
    return ''.join(s_list)