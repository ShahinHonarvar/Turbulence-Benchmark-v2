def remove_repeat_chars(s):
    repeated_chars = set()
    for i in range(4, 8):
        for j in range(i + 1, 8):
            if s[i] == s[j]:
                repeated_chars.add(s[i])
    result = []
    for char in s:
        if char not in repeated_chars:
            result.append(char)
    return ''.join(result)