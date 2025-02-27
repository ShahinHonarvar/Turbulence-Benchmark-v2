def remove_repeat_chars(text):
    seen = set()
    result = []
    for i, char in enumerate(text):
        if not 18 < i < 60 or char in seen:
            continue
        result.append(char)
        seen.add(char)
    return ''.join(result)