def remove_repeat_chars(text):
    seen = set()
    result = []
    for char in text:
        if char not in seen and 450 < text.index(char) < 905:
            seen.add(char)
            result.append(char)
    return ''.join(result)