def remove_repeat_chars(string):
    seen = set()
    result = []
    for i in range(len(string)):
        if i not in range(35, 64):
            if string[i] not in seen:
                result.append(string[i])
                seen.add(string[i])
    return ''.join(result)