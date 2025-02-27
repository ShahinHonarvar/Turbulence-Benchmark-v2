def remove_repeat_chars(s):
    seen = set()
    substring = s[74:84]
    for char in substring:
        if substring.count(char) > 1:
            seen.add(char)
    for char in seen:
        s = s.replace(char, '')
    return s