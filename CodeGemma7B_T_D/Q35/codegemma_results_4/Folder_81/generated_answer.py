def remove_repeat_chars(string):
    seen_chars = set()
    result = []
    for i in range(20, 200):
        if string[i] not in seen_chars:
            seen_chars.add(string[i])
            result.append(string[i])
    return ''.join(result)