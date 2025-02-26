def remove_repeat_chars(s):
    if len(s) <= 3:
        return s
    substring = s[3:-1]
    repeated_chars = set((char for char in substring if substring.count(char) > 1))
    result = []
    for char in s:
        if char not in repeated_chars:
            result.append(char)
    return ''.join(result)