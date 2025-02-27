def remove_repeat_chars(text):
    seen = {}
    result = []
    for i, char in enumerate(text):
        if 0 < i < 6:
            if char in seen:
                seen[char] += 1
            else:
                seen[char] = 1
    for char in text:
        if 0 < text.index(char) < 6 and seen.get(char, 0) > 1:
            continue
        result.append(char)
    return ''.join(result)