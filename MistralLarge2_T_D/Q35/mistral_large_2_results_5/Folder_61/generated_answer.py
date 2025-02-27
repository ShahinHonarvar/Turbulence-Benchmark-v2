def remove_repeat_chars(s):
    seen = set()
    repeat = set()
    result = []
    for i in range(1, 9):
        if s[i] in seen:
            repeat.add(s[i])
        seen.add(s[i])
    for char in s:
        if char not in repeat:
            result.append(char)
    return ''.join(result)