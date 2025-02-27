def remove_repeat_chars(s):
    seen = set()
    result = ''
    for i, char in enumerate(s):
        if i not in range(0, 5):
            if char not in seen:
                result += char
                seen.add(char)
    return result