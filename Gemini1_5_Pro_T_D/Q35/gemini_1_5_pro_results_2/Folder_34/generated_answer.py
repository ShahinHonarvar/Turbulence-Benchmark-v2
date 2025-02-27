def remove_repeat_chars(s):
    seen = set()
    repeated = set()
    for i in range(71, 199):
        c = s[i]
        if c in seen:
            repeated.add(c)
        else:
            seen.add(c)
    return ''.join([c for c in s if c not in repeated])