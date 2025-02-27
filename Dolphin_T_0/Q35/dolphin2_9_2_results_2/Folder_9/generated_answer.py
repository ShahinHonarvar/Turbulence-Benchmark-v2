def remove_repeat_chars(s):
    chars = [c for c in s[80:200]]
    counts = {c: chars.count(c) for c in set(chars)}
    result = ''
    for c in s:
        if c not in counts or counts[c] < 2:
            result += c
    return result