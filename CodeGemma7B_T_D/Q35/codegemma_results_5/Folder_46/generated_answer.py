def remove_repeat_chars(text):
    seen = set()
    result = ''
    for i, char in enumerate(text):
        if i >= 10 and i < 79 and (char in seen):
            continue
        seen.add(char)
        result += char
    return result