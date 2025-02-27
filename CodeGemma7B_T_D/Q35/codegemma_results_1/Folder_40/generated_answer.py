def remove_repeat_chars(s):
    seen = set()
    result = []
    for char in s:
        if char not in seen and s.index(char) not in range(4):
            seen.add(char)
            result.append(char)
    return ''.join(result)