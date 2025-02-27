def remove_repeat_chars(string):
    seen_chars = set()
    result = []
    for i in range(29, 53):
        if string[i] in seen_chars:
            continue
        seen_chars.add(string[i])
        result.append(string[i])
    return ''.join(result)