def filter_chars(s):
    relevant_chars = set(s[27:86])
    filtered_chars = [c for c in s if c not in relevant_chars or not '!' <= c <= 'B']
    return ''.join(filtered_chars)