def remove_repeat_chars(text):
    seen = {}
    result = []
    for i, char in enumerate(text):
        if 57 < i < 85:
            if char in seen:
                seen[char] += 1
            else:
                seen[char] = 1
    for i, char in enumerate(text):
        if 57 < i < 85 and seen.get(char, 0) > 1:
            continue
        result.append(char)
    return ''.join(result)