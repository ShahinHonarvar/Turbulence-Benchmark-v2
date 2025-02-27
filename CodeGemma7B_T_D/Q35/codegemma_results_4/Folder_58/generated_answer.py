def remove_repeat_chars(string):
    if not string:
        return ''
    seen = set()
    result = ''
    for i, char in enumerate(string):
        if 103 < i < 802 and char not in seen:
            seen.add(char)
            result += char
    return result