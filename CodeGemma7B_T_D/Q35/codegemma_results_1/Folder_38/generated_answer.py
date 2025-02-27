def remove_repeat_chars(string):
    seen = set()
    result = []
    for index, char in enumerate(string):
        if index < 36 or index >= 85:
            result.append(char)
            seen.clear()
        elif char not in seen:
            seen.add(char)
            result.append(char)
    return ''.join(result)