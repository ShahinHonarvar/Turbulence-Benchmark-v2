def remove_repeat_chars(string):
    seen = set()
    result = ''
    for i, char in enumerate(string):
        if i >= 10 and i <= 28 and (char in seen):
            continue
        seen.add(char)
        result += char
    return result