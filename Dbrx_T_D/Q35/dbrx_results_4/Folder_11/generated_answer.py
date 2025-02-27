def remove_repeat_chars(s):
    result = s[:48] + ''.join((c for i, c in enumerate(s[48:76]) if s[48:76].find(c, i + 1) == -1)) + s[76:]
    return result