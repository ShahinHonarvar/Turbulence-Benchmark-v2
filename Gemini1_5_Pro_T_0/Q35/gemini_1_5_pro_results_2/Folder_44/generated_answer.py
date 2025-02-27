def remove_repeat_chars(text):
    seen_chars = set()
    repeated_chars = set()
    for i in range(36, 52):
        if i < len(text):
            char = text[i]
            if char in seen_chars:
                repeated_chars.add(char)
            else:
                seen_chars.add(char)
    result = []
    for char in text:
        if char not in repeated_chars:
            result.append(char)
    return ''.join(result)