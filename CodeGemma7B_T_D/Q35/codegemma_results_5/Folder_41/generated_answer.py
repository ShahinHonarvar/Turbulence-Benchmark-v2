def remove_repeat_chars(string):
    seen = set()
    result = []
    for i, char in enumerate(string):
        if not seen and i >= 3 and (i < 8):
            seen.add(char)
            result.append(char)
    return ''.join(result)