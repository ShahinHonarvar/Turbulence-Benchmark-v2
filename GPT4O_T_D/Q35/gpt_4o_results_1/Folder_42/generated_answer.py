def remove_repeat_chars(s):
    if len(s) <= 60:
        return s
    substring = s[19:60]
    unique_chars = set((char for char in substring if substring.count(char) > 1))
    result = []
    for char in s:
        if not (char in unique_chars and 19 < s.index(char) < 60):
            result.append(char)
    return ''.join(result)