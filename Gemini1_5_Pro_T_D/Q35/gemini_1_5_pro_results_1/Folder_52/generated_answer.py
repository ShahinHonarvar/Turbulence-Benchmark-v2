def remove_repeat_chars(text):
    seen_chars = set()
    result = []
    for i, char in enumerate(text):
        if 38 < i < 81:
            if char in seen_chars:
                continue
            elif text[38:81].count(char) > 1:
                seen_chars.add(char)
                continue
        result.append(char)
    return ''.join(result)