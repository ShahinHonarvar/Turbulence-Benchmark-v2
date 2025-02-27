def remove_repeat_chars(s):
    seen = set()
    result = []
    for i, char in enumerate(s):
        if i >= 39 and i <= 43:
            if char not in seen:
                seen.add(char)
                result.append(char)
            else:
                continue
        else:
            result.append(char)
    return ''.join(result)