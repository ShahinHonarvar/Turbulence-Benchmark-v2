def remove_repeat_chars(string):
    chars = set()
    result = []
    for char in string[48:76]:
        if char in chars:
            continue
        chars.add(char)
        result.append(char)
    return ''.join(result)