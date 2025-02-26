def remove_repeat_chars(s):
    if len(s) <= 19:
        return s
    segment = s[19:60]
    repeat_chars = set()
    for char in segment:
        if segment.count(char) > 1 and char not in repeat_chars:
            repeat_chars.add(char)
    result = s[:19] + ''.join((char for char in segment if char not in repeat_chars)) + s[60:]
    return result