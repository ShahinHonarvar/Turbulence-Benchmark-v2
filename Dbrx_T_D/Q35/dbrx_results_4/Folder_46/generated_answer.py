def remove_repeat_chars(string):
    used_char = set()
    result = ''
    for i in range(len(string)):
        if i >= 10 and i < 79 and (string[i] in used_char):
            continue
        result += string[i]
        if string[i] not in used_char:
            used_char.add(string[i])
    return result