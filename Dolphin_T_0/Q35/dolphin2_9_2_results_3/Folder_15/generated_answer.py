def remove_repeat_chars(s):
    indices = set()
    for i in range(5):
        if s[i] in s[i + 1:i + 5]:
            indices.add(s.index(s[i]))
    result = ''
    for i in range(len(s)):
        if i not in indices:
            result += s[i]
    return result