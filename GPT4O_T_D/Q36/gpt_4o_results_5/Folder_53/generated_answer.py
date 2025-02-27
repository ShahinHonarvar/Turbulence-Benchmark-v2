def filter_chars(s):
    if len(s) <= 90:
        return s
    filtered = list(s)
    for i in range(91, min(97, len(s))):
        if 'j' < s[i] < 'w':
            filtered = [char for char in filtered if char != s[i]]
    return ''.join(filtered)