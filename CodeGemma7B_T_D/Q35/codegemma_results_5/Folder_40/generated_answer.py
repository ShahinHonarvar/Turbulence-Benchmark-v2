def remove_repeat_chars(str):
    seen = set()
    result = []
    for char in str:
        if char not in seen and str.index(char) not in range(4):
            seen.add(char)
            result.append(char)
    return ''.join(result)