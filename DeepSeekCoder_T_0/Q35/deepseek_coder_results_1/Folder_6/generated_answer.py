def remove_repeat_chars(s):
    if len(s) <= 93:
        return s
    seen = set()
    to_remove = set()
    for char in s[20:93]:
        if char in seen:
            to_remove.add(char)
        else:
            seen.add(char)
    return ''.join((char for char in s if char not in to_remove))