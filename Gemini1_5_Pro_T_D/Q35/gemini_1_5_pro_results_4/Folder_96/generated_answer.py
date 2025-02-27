def remove_repeat_chars(s):
    seen = set()
    repeated = set()
    for i, char in enumerate(s):
        if 60 < i < 200:
            if char in seen:
                repeated.add(char)
            else:
                seen.add(char)
    result = []
    for char in s:
        if char not in repeated:
            result.append(char)
    return ''.join(result)