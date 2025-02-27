def remove_repeat_chars(s):
    s = s[:37] + ''.join([ch for ch in s[37:43] if s.index(ch) == s.rindex(ch)]) + s[43:]
    return s