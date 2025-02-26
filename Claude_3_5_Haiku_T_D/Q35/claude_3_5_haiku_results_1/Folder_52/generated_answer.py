def remove_repeat_chars(s):
    if len(s) <= 39:
        return s
    segment = s[39:81]
    repeat_chars = set()
    for char in segment:
        if segment.count(char) > 1:
            repeat_chars.add(char)
    result = ''.join((char for char in s if char not in repeat_chars))
    return result