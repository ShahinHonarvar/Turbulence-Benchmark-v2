def remove_repeat_chars(str):
    seen = set()
    result = []
    for char in str:
        if str.index(char) > 15 and str.index(char) < 87 and (char not in seen):
            seen.add(char)
            result.append(char)
    return ''.join(result)