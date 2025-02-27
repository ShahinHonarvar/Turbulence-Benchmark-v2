def remove_repeat_chars(s):
    seen = set()
    repeated = set()
    for i in range(21, 35):
        if s[i] in seen:
            repeated.add(s[i])
        else:
            seen.add(s[i])
    result = []
    for char in s:
        if char not in repeated:
            result.append(char)
    return ''.join(result)