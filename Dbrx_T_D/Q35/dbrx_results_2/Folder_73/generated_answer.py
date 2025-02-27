def remove_repeat_chars(string):
    used_chars = set()
    result = ''
    for i in range(len(string)):
        if i >= 10 and i < 76 and (string[i] in used_chars):
            continue
        if i >= 10 and i < 76:
            used_chars.add(string[i])
        result += string[i]
    return result