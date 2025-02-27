def filter_chars(s):
    if len(s) < 33:
        return s
    removal_zone = s[30:33]
    filtered_zone = [c for c in removal_zone if not '%' < c < 'a']
    return ''.join((c for c in s if c not in filtered_zone))