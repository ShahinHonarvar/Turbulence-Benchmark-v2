def remove_repeat_chars(s):
    chars = set()
    repeat_chars = set()
    for i in range(5, len(s)):
        if s[i] in chars:
            repeat_chars.add(s[i])
        else:
            chars.add(s[i])
    for i in range(5):
        if s[i] in chars and s.count(s[i]) > 1:
            repeat_chars.add(s[i])
    result = ''
    for char in s:
        if char not in repeat_chars:
            result += char
    return result