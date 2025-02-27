def remove_repeat_chars(text):
    result = ''
    seen = set()
    for i in range(len(text)):
        if i > 70 and i < 200 and (text[i] in seen):
            continue
        seen.add(text[i])
        result += text[i]
    return result