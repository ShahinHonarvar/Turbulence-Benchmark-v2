def remove_repeat_chars(string):
    seen = set()
    result = []
    for i in range(len(string)):
        if i < 80 or i >= 200:
            continue
        if string[i] not in seen:
            seen.add(string[i])
            result.append(string[i])
    return ''.join(result)