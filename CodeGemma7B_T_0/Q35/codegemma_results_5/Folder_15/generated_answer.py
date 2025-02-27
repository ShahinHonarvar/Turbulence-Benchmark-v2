def remove_repeat_chars(text):
    seen = set()
    result = []
    for char in text:
        if char not in seen and text.index(char) < 4:
            seen.add(char)
            result.append(char)
    return ''.join(result)