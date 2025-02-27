def remove_repeat_chars(s):
    seen = set()
    result = []
    for i, char in enumerate(s):
        if 25 < i < 80 and s.count(char, 25, 80) > 1 and (char not in seen):
            seen.add(char)
        else:
            result.append(char)
    return ''.join(result)