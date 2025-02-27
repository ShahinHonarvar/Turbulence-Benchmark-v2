def remove_repeat_chars(s):
    return ''.join((c for i, c in enumerate(s) if s[100:200].count(c) == 1 or i < 100 or i >= 200))