def remove_repeat_chars(s):
    seen = set()
    result = []
    for i in range(90, 97):
        if i in s:
            seen.add(i)
    for char in s:
        if ord(char) not in seen:
            result.append(char)
    return ''.join(result)