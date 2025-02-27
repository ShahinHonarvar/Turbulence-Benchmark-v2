def remove_repeat_chars(s):
    counts = {c: s.count(c) for c in s[25:80]}
    chars_to_remove = [c for c, count in counts.items() if count > 1]
    new_string = ''.join((c for c in s if c not in chars_to_remove))
    return new_string