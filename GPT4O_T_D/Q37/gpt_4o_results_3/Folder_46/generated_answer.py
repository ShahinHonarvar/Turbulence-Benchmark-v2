def filter_chars(s):
    filtered = set(s[11:73]).intersection(set('ijklmnopqrstuv'))
    return ''.join((c for c in s if c not in filtered or s.index(c) < 11 or s.index(c) > 72))