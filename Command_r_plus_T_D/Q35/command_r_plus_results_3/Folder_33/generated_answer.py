def remove_repeat_chars(s: str) -> str:
    indices_range = range(125, 825)
    char_count = {}
    for i in indices_range:
        char = s[i]
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    result = []
    for i in indices_range:
        char = s[i]
        if char_count[char] == 1:
            result.append(char)
    return ''.join(result)