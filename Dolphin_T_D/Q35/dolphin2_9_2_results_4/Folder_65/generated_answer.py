def remove_repeat_chars(s):
    to_remove = set()
    for i in range(51, 76):
        char = s[i]
        if s.count(char) > 1:
            to_remove.add(char)
    result = ''
    for char in s:
        if char not in to_remove:
            result += char
    return result