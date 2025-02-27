def remove_repeat_chars(s):
    return ''.join((c for c in s if s.index(c) >= 44 and s.index(c) <= 91 and (s.index(c) == s.rindex(c))))