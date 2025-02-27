def remove_repeat_chars(text):
    seen = set()
    result = ''
    for char in text:
        if text.index(char) not in range(5):
            if char not in seen:
                seen.add(char)
                result += char
    return result