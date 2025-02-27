def remove_repeat_chars(string):
    result = ''
    seen_chars = set()
    for i, char in enumerate(string):
        if i >= 20 and i < 51 and (char in seen_chars):
            continue
        seen_chars.add(char)
        result += char
    return result