def remove_repeat_chars(s):
    seen = set()
    result = []
    for c in s:
        if c not in seen and 0 < ord(c) - ord('a') < 6:
            seen.add(c)
            result.append(c)
    return ''.join(result)