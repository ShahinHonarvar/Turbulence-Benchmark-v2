def remove_repeat_chars(text):
    seen = set()
    result = []
    for i, char in enumerate(text):
        if 69 < i < 97 and char in seen:
            continue
        seen.add(char)
        result.append(char)
    return ''.join(result)