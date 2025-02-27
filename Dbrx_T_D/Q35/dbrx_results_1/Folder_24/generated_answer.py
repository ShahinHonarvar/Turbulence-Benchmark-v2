def remove_repeat_chars(string):
    used_chars = set()
    result = ''
    for i in range(len(string)):
        if i < 13 or i >= 91:
            result += string[i]
        elif string[i] not in used_chars:
            used_chars.add(string[i])
            result += string[i]
    return result