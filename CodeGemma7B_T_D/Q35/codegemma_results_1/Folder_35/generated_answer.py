def remove_repeat_chars(str):
    seen = set()
    result = []
    for i in range(len(str)):
        if i >= 77 and i < 84:
            if str[i] not in seen:
                seen.add(str[i])
                result.append(str[i])
        else:
            result.append(str[i])
    return ''.join(result)