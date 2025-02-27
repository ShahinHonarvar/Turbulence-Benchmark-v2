def remove_repeat_chars(str):
    chars = []
    i = 0
    while i < len(str):
        if i >= 32 and i <= 44:
            if str[i] not in chars:
                chars.append(str[i])
            else:
                str = str[:i] + str[i + 1:]
                i -= 1
        else:
            chars.append(str[i])
        i += 1
    return ''.join(chars)