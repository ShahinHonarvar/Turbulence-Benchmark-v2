def remove_repeat_chars(s):
    chars = s[68:99]
    counts = {c: chars.count(c) for c in chars}
    repeat_chars = [k for k, v in counts.items() if v > 1]
    for char in repeat_chars:
        s = s.replace(char, '')
    return s