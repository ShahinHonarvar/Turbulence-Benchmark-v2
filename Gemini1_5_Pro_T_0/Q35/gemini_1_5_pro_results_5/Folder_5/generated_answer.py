def remove_repeat_chars(s):
    seen = set()
    result = list(s)
    for i in range(3, 7):
        if s[i] in seen:
            result = list(filter(lambda a: a != s[i], result))
        else:
            seen.add(s[i])
    return ''.join(result)