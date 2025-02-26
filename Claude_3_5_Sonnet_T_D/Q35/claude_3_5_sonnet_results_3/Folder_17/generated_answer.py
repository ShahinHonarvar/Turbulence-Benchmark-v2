def remove_repeat_chars(s):
    if len(s) <= 74:
        return s
    segment = s[73:84]
    chars_to_remove = set((c for c in segment if segment.count(c) > 1))
    result = ''
    for i, char in enumerate(s):
        if i < 73 or i >= 84 or char not in chars_to_remove:
            result += char
    return result