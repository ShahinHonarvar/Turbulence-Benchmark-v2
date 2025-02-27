def remove_repeat_chars(str):
    seen_chars = set()
    res = ''
    for i in range(len(str)):
        if i < 36 or i > 85:
            res += str[i]
        elif str[i] not in seen_chars:
            seen_chars.add(str[i])
            res += str[i]
    return res