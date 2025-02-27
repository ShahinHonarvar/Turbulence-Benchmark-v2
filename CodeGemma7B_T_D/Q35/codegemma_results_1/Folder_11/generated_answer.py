def remove_repeat_chars(string):
    result = ''
    for i in range(len(string)):
        if i < 48 or i >= 76:
            result += string[i]
    seen = set()
    for i in range(48, 76):
        char = string[i]
        if char not in seen:
            seen.add(char)
            result += char
    return result