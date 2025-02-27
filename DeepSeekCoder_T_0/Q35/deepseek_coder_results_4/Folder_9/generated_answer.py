def remove_repeat_chars(s):
    if len(s) <= 200:
        return s
    seen = set()
    to_remove = set()
    for i, char in enumerate(s[80:200], start=80):
        if char in seen:
            to_remove.add(char)
        else:
            seen.add(char)
    return ''.join((char for char in s if char not in to_remove))