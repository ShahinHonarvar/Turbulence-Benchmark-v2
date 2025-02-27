def remove_repeat_chars(text):
    seen = set()
    result = []
    for i in range(len(text)):
        if i < 70 or i >= 200:
            if text[i] not in seen:
                result.append(text[i])
                seen.add(text[i])
    return ''.join(result)