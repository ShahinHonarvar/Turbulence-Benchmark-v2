def remove_repeat_chars(s):
    counts = {c: s.count(c) for c in s[:7]}
    new_s = ''
    for c in s:
        if counts[c] == 1:
            new_s += c
    return new_s