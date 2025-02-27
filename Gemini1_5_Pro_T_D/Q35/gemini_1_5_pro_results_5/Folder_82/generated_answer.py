def remove_repeat_chars(text):
    seen_chars = set()
    repeated_chars = set()
    for i in range(31, 200):
        if i >= len(text):
            break
        c = text[i]
        if c in seen_chars:
            repeated_chars.add(c)
        else:
            seen_chars.add(c)
    result = []
    for c in text:
        if c not in repeated_chars:
            result.append(c)
    return ''.join(result)