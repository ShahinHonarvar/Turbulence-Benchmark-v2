def remove_repeat_chars(string):
    used_chars = set()
    result = []
    for char in string[1:-1]:
        if char not in used_chars:
            result.append(char)
            used_chars.add(char)
    return ''.join(result)