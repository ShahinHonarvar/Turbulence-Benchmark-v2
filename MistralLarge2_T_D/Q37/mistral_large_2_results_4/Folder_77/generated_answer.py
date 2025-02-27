def filter_chars(s):
    to_remove = {s[i] for i in range(len(s)) if 384 <= i <= 411 and '/' <= s[i] <= '8'}
    return ''.join((c for c in s if c not in to_remove))