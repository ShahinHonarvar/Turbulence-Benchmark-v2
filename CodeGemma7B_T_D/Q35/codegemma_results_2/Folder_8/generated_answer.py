def remove_repeat_chars(s):
    seen = set()
    result = []
    for i, char in enumerate(s):
        if i >= 45 and i <= 48:
            if char not in seen:
                seen.add(char)
                result.append(char)
        else:
            result.append(char)
    return ''.join(result)