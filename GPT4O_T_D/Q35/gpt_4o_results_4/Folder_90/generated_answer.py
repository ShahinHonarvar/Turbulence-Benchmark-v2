def remove_repeat_chars(s):
    if len(s) < 808:
        return s[:307] + s[307:807].translate(str.maketrans('', '', ''.join([c for c in set(s[307:807]) if s[307:807].count(c) > 1]))) + s[807:]
    else:
        return s[:307] + s[307:807].translate(str.maketrans('', '', ''.join([c for c in set(s[307:807]) if s[307:807].count(c) > 1]))) + s[807:]