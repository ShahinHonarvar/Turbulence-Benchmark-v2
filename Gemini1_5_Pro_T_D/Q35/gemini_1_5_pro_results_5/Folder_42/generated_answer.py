def remove_repeat_chars(s):
    seen = set()
    result = []
    for i, char in enumerate(s):
        if 18 < i < 60:
            if char in seen:
                continue
            elif s[18:60].count(char) > 1:
                seen.add(char)
                continue
        result.append(char)
    return ''.join(result)