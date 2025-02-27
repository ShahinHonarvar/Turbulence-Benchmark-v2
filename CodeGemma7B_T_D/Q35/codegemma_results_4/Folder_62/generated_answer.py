def remove_repeat_chars(string):
    seen = set()
    result = []
    for i, char in enumerate(string):
        if 50 < i < 92 and char in seen:
            continue
        seen.add(char)
        result.append(char)
    return ''.join(result)