def remove_repeat_chars(s):
    start, end = (36, 54)
    repeat_chars = set()
    for char in s[start:end]:
        if s[start:end].count(char) > 1:
            repeat_chars.add(char)
    result = []
    for char in s:
        if char not in repeat_chars:
            result.append(char)
    return ''.join(result)