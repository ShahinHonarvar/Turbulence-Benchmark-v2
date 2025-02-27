def remove_repeat_chars(text):
    seen = set()
    result = []
    for i in range(len(text)):
        if i not in range(330, 543):
            if text[i] not in seen:
                seen.add(text[i])
                result.append(text[i])
    return ''.join(result)