def remove_repeat_chars(s):
    if len(s) <= 200:
        return s
    to_remove = set()
    segment = s[51:200]
    for char in segment:
        if segment.count(char) > 1:
            to_remove.add(char)
    result = ''.join((c for c in s if c not in to_remove))
    return result