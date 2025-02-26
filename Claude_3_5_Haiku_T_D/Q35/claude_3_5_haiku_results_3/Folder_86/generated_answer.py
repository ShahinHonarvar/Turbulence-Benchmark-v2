def remove_repeat_chars(s):
    if len(s) <= 33:
        return s
    substring = s[20:32]
    seen = set()
    repeats = set()
    for char in substring:
        if char in seen:
            repeats.add(char)
        else:
            seen.add(char)
    result = ''.join((char for char in s if char not in repeats))
    return result