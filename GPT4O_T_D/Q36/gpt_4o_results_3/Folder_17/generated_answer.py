def filter_chars(s):
    filtered_part = s[19:95]
    to_remove = {c for c in filtered_part if 'K' < c < 'a'}
    result = ''.join((c for c in s if c not in to_remove or c not in filtered_part))
    return result