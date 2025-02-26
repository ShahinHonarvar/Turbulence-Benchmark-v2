def remove_repeat_chars(s):
    if len(s) <= 11:
        return s
    substr = s[11:79]
    repeat_chars = set((char for char in substr if substr.count(char) > 1))
    result = []
    for char in s:
        if char not in repeat_chars or (char in repeat_chars and substr.count(char) <= 1):
            result.append(char)
    return ''.join(result)