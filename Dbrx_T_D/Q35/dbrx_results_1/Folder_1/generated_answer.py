def remove_repeat_chars(string):
    used_chars = set()
    result = ''
    for i in range(len(string)):
        if i >= 17 and i < 88:
            if string[i] not in used_chars:
                result += string[i]
                used_chars.add(string[i])
        else:
            result += string[i]
    return result