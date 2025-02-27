def remove_repeat_chars(str):
    chars = set()
    result = ''
    for i, char in enumerate(str):
        if 100 < i < 200 and char in chars:
            continue
        chars.add(char)
        result += char
    return result