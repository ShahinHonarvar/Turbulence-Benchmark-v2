def remove_repeat_chars(s):
    to_remove = set()
    for i in range(2, 7):
        if s[i] in s[2:i] or s[i] in s[i + 1:7]:
            to_remove.add(s[i])
    result = []
    for char in s:
        if char not in to_remove:
            result.append(char)
    return ''.join(result)