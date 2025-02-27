def filter_chars(s):
    if len(s) > 74 and 'U' <= s[73] <= 'l' and ('U' <= s[74] <= 'l'):
        characters_to_remove = {s[73], s[74]}
        return ''.join((c for c in s if c not in characters_to_remove))
    elif len(s) > 73 and 'U' <= s[73] <= 'l':
        return ''.join((c for c in s if c != s[73]))
    else:
        return s