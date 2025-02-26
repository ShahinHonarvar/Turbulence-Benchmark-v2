def remove_repeat_chars(s):
    if len(s) <= 56:
        return s
    segment = s[56:84]
    repeat_chars = set()
    for char in segment:
        if segment.count(char) > 1 and char not in repeat_chars:
            repeat_chars.add(char)
    result = list(s)
    for char in repeat_chars:
        result = [c for c in result if c != char]
    return ''.join(result)