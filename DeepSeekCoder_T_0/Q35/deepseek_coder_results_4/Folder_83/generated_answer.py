def remove_repeat_chars(s):
    if len(s) <= 200:
        return s
    seen = set()
    to_remove = set()
    for char in s[100:200]:
        if char in seen:
            to_remove.add(char)
        else:
            seen.add(char)
    return ''.join((char for char in s if char not in to_remove))