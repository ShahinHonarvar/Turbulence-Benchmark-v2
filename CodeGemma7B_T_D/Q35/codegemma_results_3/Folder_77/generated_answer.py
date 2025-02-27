def remove_repeat_chars(s):
    return ''.join((c for i, c in enumerate(s) if not (355 <= i < 988 and s[i] == c)))