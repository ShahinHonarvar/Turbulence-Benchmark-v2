def remove_repeat_chars(s):
    seen = set()
    result = []
    for i, char in enumerate(s):
        if i > 72 and i < 93 and (char in s[73:93]) and (char not in seen):
            seen.add(char)
        else:
            result.append(char)
    return ''.join(result)