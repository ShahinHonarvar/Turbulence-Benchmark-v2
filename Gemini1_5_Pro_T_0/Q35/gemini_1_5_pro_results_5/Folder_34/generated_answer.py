def remove_repeat_chars(s):
    seen_chars = set()
    repeated_chars = set()
    for i in range(71, 199):
        char = s[i]
        if char in seen_chars:
            repeated_chars.add(char)
        else:
            seen_chars.add(char)
    result = []
    for char in s:
        if char not in repeated_chars:
            result.append(char)
    return ''.join(result)