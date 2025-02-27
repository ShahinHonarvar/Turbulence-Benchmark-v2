def remove_repeat_chars(s):
    substring = s[73:84]
    seen = set()
    repeated_chars = set()
    for char in substring:
        if char in seen:
            repeated_chars.add(char)
        else:
            seen.add(char)
    result = ''.join((char for char in s if char not in repeated_chars))
    return result