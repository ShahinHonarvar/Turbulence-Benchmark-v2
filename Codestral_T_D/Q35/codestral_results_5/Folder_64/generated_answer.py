def remove_repeat_chars(s):
    seen = set()
    result = []
    for char in s:
        if s.index(char) < 6 and s.count(char) > 1 and (char not in seen):
            seen.add(char)
        else:
            result.append(char)
    return ''.join(result)