def remove_repeat_chars(s):
    seen = set()
    result = []
    for i, char in enumerate(s):
        if i >= 355 and i <= 988 and (char in seen):
            continue
        seen.add(char)
        result.append(char)
    return ''.join(result)