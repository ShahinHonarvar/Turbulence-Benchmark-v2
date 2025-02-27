def remove_repeat_chars(text):
    seen = set()
    result = []
    for i, char in enumerate(text):
        if i < 16 or i >= 87:
            continue
        if char not in seen:
            seen.add(char)
            result.append(char)
    return ''.join(result)