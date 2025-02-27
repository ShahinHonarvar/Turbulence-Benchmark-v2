def remove_repeat_chars(text):
    seen_chars = set()
    result = ''
    for i, char in enumerate(text):
        if 27 < i < 96:
            if char in seen_chars:
                continue
            elif text[28:96].count(char) > 1:
                seen_chars.add(char)
                continue
        result += char
    return result