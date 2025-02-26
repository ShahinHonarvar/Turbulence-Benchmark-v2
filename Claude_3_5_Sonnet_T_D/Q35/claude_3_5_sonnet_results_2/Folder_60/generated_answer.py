def remove_repeat_chars(s):
    repeated_chars = set()
    for i in range(39, 52):
        if s[i] in s[39:52] and s[i] not in repeated_chars:
            repeated_chars.add(s[i])
    return ''.join((char for char in s if char not in repeated_chars))