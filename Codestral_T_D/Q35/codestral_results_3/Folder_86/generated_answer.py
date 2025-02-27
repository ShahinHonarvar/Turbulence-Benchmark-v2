def remove_repeat_chars(s):
    seen = set()
    repeat = set()
    result = []
    for char in s[19:32]:
        if char in seen:
            repeat.add(char)
        seen.add(char)
    for char in s:
        if char not in repeat:
            result.append(char)
    return ''.join(result)