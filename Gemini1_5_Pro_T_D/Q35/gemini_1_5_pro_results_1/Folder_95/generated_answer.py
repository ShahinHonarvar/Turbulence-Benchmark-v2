def remove_repeat_chars(s):
    seen = set()
    substring = s[32:99]
    for c in substring:
        if substring.count(c) > 1:
            seen.add(c)
    result = []
    for c in s:
        if c not in seen:
            result.append(c)
    return ''.join(result)