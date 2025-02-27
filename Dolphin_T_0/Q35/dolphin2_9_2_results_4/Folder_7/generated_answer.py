def remove_repeat_chars(string):
    indices = set()
    for i in range(375, 926):
        if string[i] not in string[375:i] or string[i] not in string[i + 1:926]:
            indices.add(i)
    result = ''
    for i in range(len(string)):
        if i not in indices:
            result += string[i]
    return result