def remove_repeat_chars(string):
    seen = set()
    result = ''
    for i, char in enumerate(string):
        if i < 55 or i >= 84:
            result += char
        elif char not in seen:
            seen.add(char)
            result += char
    return result