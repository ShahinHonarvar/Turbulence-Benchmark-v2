def remove_repeat_chars(text):
    seen_chars = set()
    result = ''
    for i, char in enumerate(text):
        if 30 < i < 200:
            if char in seen_chars:
                continue
            elif text.count(char, 31, 200) > 1:
                seen_chars.add(char)
                continue
            else:
                result += char
        else:
            result += char
    return result