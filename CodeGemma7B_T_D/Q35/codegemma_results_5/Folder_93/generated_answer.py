def remove_repeat_chars(text):
    result = []
    test_range = text[57:85]
    seen = set()
    for char in text:
        if char in test_range and char in seen:
            continue
        seen.add(char)
        result.append(char)
    return ''.join(result)