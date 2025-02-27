def remove_repeat_chars(s):
    seen_chars = set()
    repeated_chars = set()
    for i in range(71, 200):
        if s[i] in seen_chars:
            repeated_chars.add(s[i])
        else:
            seen_chars.add(s[i])
    result = []
    for char in s:
        if char not in repeated_chars:
            result.append(char)
    return ''.join(result)