def remove_repeat_chars(string):
    used_chars = set()
    result = ''
    for i, char in enumerate(string):
        if 50 < i < 76:
            if char in used_chars:
                continue
            else:
                used_chars.add(char)
        result += char
    return result