def remove_repeat_chars(s):
    seen = set()
    repeated = set()
    for i in range(11, 76):
        c = s[i]
        if c in seen:
            repeated.add(c)
        else:
            seen.add(c)
    output = []
    for c in s:
        if c not in repeated:
            output.append(c)
    return ''.join(output)