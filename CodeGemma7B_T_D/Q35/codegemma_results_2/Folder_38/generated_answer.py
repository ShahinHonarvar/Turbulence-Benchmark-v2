def remove_repeat_chars(text):
    seen = set()
    result = []
    for idx, char in enumerate(text):
        if idx >= 36 and idx < 85 and (char in seen):
            continue
        seen.add(char)
        result.append(char)
    return ''.join(result)