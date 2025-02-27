def remove_repeat_chars(s):
    seen = set()
    result = []
    for i, char in enumerate(s):
        if 44 < i < 78:
            if char in seen:
                continue
            elif s[45:78].count(char) > 1:
                seen.add(char)
                continue
        result.append(char)
    return ''.join(result)