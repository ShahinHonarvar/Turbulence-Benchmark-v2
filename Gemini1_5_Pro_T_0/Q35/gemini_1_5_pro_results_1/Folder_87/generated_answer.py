def remove_repeat_chars(text):
    seen_chars = set()
    result = []
    for i, char in enumerate(text):
        if 20 < i < 43:
            if char in seen_chars:
                continue
            else:
                seen_chars.add(char)
        result.append(char)
    return ''.join(result)