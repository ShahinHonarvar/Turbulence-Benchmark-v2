def remove_repeat_chars(s):
    if len(s) <= 21:
        return s
    sub_str = s[21:43]
    result = []
    for char in sub_str:
        if sub_str.count(char) == 1:
            result.append(char)
    return s[:21] + ''.join(result) + s[43:]