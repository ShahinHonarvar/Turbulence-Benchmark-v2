def remove_repeat_chars(s):
    if len(s) <= 18:
        return s
    segment = s[19:60]
    repeats = set()
    for char in segment:
        if segment.count(char) > 1 and char not in repeats:
            repeats.add(char)
    result = s[0:19] + ''.join((char for char in segment if char not in repeats)) + s[60:]
    return result