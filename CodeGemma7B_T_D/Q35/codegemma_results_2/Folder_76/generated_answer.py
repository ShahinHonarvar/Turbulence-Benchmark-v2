def remove_repeat_chars(str):
    result = []
    seen_chars = set()
    for i in range(330, 543):
        if str[i] not in seen_chars:
            result.append(str[i])
            seen_chars.add(str[i])
    return ''.join(result)