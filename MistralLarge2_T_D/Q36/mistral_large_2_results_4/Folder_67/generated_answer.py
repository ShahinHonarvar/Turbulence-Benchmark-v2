def filter_chars(s):
    chars_to_filter = {s[i] for i in range(18, 31) if 'H' < s[i] < '|'}
    return ''.join((c for c in s if c not in chars_to_filter))