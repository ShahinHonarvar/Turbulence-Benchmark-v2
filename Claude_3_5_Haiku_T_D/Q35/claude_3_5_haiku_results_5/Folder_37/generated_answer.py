def remove_repeat_chars(s):
    if len(s) <= 3:
        return s
    substring = s[3:7]
    repeat_chars = set((char for char in substring if substring.count(char) > 1))
    result = []
    for char in s:
        if char not in repeat_chars or (char in repeat_chars and s.index(char) <= 2):
            result.append(char)
    return ''.join(result)