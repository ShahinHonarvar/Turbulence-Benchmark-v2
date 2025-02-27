def remove_repeat_chars(text):
    seen_chars = set()
    repeated_chars = set()
    for i in range(34, 69):
        if text[i] in seen_chars:
            repeated_chars.add(text[i])
        else:
            seen_chars.add(text[i])
    result = []
    for char in text:
        if char not in repeated_chars:
            result.append(char)
    return ''.join(result)