def remove_repeat_chars(string):
    seen = set()
    result = []
    for i, char in enumerate(string[19:32]):
        if char not in seen:
            seen.add(char)
            result.append(char)
    for i, char in enumerate(string):
        if char in seen and i not in range(19, 32):
            result.append(char)
    return ''.join(result)