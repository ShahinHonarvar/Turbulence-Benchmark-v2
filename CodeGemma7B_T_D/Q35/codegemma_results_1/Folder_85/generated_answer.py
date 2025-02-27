def remove_repeat_chars(str):
    """remove repeated character between index 1 and 8"""
    seen = set()
    result = ''
    for i in range(1, 8):
        if str[i] not in seen:
            result += str[i]
            seen.add(str[i])
    return result