def remove_repeat_chars(text):
    seen_chars = set()
    result = []
    for i, char in enumerate(text):
        if 17 < i < 88:
            if char in seen_chars:
                continue
            else:
                seen_chars.add(char)
        result.append(char)
    return ''.join(result)