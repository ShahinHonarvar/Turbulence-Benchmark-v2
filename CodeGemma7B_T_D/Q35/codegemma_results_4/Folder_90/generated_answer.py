def remove_repeat_chars(text):
    seen_chars = set()
    result = []
    for i, char in enumerate(text):
        if 306 <= i < 807 and char in seen_chars:
            continue
        seen_chars.add(char)
        result.append(char)
    return ''.join(result)