def remove_repeat_chars(string):
    used_chars = set()
    result = []
    for char in string[1:10]:
        if char not in used_chars:
            used_chars.add(char)
            result.append(char)
    return ''.join(result) + string[10:]