def remove_repeat_chars(s):
    if len(s) <= 3:
        return s
    substr = s[3:-1]
    repeated_chars = set()
    for i in range(len(substr)):
        for j in range(i + 1, len(substr)):
            if substr[i] == substr[j] and substr[i] not in repeated_chars:
                repeated_chars.add(substr[i])
    result = []
    for char in s:
        if char not in repeated_chars:
            result.append(char)
        elif s.index(char) < 3 or s.index(char) >= len(s) - 1:
            result.append(char)
    return ''.join(result)