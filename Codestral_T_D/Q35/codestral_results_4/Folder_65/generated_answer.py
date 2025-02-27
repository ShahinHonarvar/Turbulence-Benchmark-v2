def remove_repeat_chars(s):
    chars = s[51:76]
    seen = set()
    result = ''
    for char in s:
        if char in chars and char not in seen:
            result += char
            seen.add(char)
        elif char not in chars:
            result += char
    return result