def filter_chars(s):
    filtered_section = {c for c in s[32:70] if 'B' < c < 'v'}
    return ''.join((c for c in s if c not in filtered_section))