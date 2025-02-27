def remove_repeat_chars(text):
    seen = set()
    result = []
    for i, char in enumerate(text):
        if i >= 20 and i <= 36:
            if char not in seen:
                result.append(char)
                seen.add(char)
    return ''.join(result)