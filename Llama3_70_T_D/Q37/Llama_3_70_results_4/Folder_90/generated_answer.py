def filter_chars(s):
    filtered_chars = set()
    for i in range(348, 853):
        if 'J' <= s[i] <= 'b':
            filtered_chars.add(s[i])
    return ''.join((c for c in s if c not in filtered_chars))