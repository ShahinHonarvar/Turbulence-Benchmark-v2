def remove_repeat_chars(s):
    seen = set()
    remove_chars = set()
    for i in range(306, 807):
        if s[i] in seen:
            remove_chars.add(s[i])
        else:
            seen.add(s[i])
    result = ''.join([c for c in s if c not in remove_chars])
    return result