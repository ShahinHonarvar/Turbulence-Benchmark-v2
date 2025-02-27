def remove_repeat_chars(s):
    seen = set()
    result = []
    for i, char in enumerate(s):
        if 46 < i < 91 and s.count(char, 46, 91) > 1 and (char not in seen):
            seen.add(char)
        else:
            result.append(char)
    return ''.join(result)