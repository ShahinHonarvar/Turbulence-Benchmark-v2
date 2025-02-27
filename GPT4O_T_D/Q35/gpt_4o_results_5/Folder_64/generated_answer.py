def remove_repeat_chars(s):
    segment = s[1:5]
    repeats = {c for c in segment if segment.count(c) > 1}
    return ''.join((c for c in s if c not in repeats))