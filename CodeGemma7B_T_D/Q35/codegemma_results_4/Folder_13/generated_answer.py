def remove_repeat_chars(str):
    seen = set()
    result = []
    for c in str:
        if c not in seen and 46 < str.index(c) < 91:
            seen.add(c)
            result.append(c)
    return ''.join(result)