def remove_repeat_chars(s):
    counts = {ch: s[62:96].count(ch) for ch in s[62:96]}
    chars_to_remove = [ch for ch, count in counts.items() if count > 1]
    for ch in chars_to_remove:
        s = s.replace(ch, '')
    return s