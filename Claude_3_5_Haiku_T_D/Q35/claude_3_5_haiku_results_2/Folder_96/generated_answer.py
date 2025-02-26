def remove_repeat_chars(s):
    if len(s) <= 60:
        return s
    segment = s[61:200]
    seen_chars = set()
    repeat_chars = set()
    for char in segment:
        if char in seen_chars:
            repeat_chars.add(char)
        else:
            seen_chars.add(char)
    result = ''.join((char for char in s if char not in repeat_chars))
    return result