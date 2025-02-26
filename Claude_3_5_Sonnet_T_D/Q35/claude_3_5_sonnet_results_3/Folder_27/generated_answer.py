def remove_repeat_chars(s):
    if len(s) <= 87:
        return s
    substr = s[87:89]
    repeats = set((c for c in substr if substr.count(c) > 1))
    result = ''
    for i, char in enumerate(s):
        if i < 87 or i >= 89 or char not in repeats:
            result += char
    return result