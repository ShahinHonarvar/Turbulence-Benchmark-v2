def remove_repeat_chars(str):
    seen = set()
    result = ''
    for i in range(len(str)):
        if i < 306 or i >= 807:
            result += str[i]
        elif str[i] not in seen:
            seen.add(str[i])
            result += str[i]
    return result