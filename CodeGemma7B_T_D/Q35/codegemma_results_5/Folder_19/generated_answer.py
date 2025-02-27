def remove_repeat_chars(text):
    seen_chars = set()
    result = []
    for i, char in enumerate(text):
        if i in range(1, 4):
            if char not in seen_chars:
                result.append(char)
                seen_chars.add(char)
    return ''.join(result)