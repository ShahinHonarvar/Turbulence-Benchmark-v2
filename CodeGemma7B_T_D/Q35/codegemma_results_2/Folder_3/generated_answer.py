def remove_repeat_chars(string):
    seen = set()
    result = []
    for i in range(56, 88):
        if string[i] not in seen:
            seen.add(string[i])
            result.append(string[i])
    return ''.join(result)