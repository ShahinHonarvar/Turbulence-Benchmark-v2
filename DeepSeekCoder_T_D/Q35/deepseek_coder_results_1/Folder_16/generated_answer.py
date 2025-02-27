def remove_repeat_chars(s):
    to_remove = set()
    for i in range(91, 97):
        if s[i] in s[91:i] or s[i] in s[i + 1:97]:
            to_remove.add(s[i])
    result = []
    for char in s:
        if char not in to_remove:
            result.append(char)
    return ''.join(result)