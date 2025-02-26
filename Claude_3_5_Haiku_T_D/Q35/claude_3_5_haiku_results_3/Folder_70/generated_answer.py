def remove_repeat_chars(s):
    if len(s) <= 44:
        return s
    segment = s[44:70]
    repeat_chars = set()
    for char in segment:
        if segment.count(char) > 1 and char not in repeat_chars:
            repeat_chars.add(char)
    result = list(s)
    for char in repeat_chars:
        result = [x for x in result if x != char]
    return ''.join(result)