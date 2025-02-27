def remove_repeat_chars(s):
    seen = set()
    repeated = set()
    for i in range(36, 85):
        if s[i] in seen:
            repeated.add(s[i])
        else:
            seen.add(s[i])
    result = []
    for i in range(len(s)):
        if s[i] not in repeated:
            result.append(s[i])
    return ''.join(result)