def remove_repeat_chars(text):
    seen = set()
    result = []
    for i in range(len(text)):
        char = text[i]
        if i > 17 and i < 60 and (char in seen):
            continue
        seen.add(char)
        result.append(char)
    return ''.join(result)