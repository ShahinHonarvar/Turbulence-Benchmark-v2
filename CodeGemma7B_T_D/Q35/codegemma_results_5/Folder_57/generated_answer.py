def remove_repeat_chars(str):
    result = ''
    seen = set()
    for i, char in enumerate(str):
        if i < 25 or i >= 80:
            if char not in seen:
                result += char
                seen.add(char)
    return result