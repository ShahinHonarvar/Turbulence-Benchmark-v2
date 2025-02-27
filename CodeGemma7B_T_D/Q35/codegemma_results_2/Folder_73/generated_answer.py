def remove_repeat_chars(string):
    seen_chars = set()
    result = []
    for i in range(10, 76):
        char = string[i]
        if char not in seen_chars:
            seen_chars.add(char)
            result.append(char)
    return ''.join(result)