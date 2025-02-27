def filter_chars(s):
    filtered = [s[i] for i in range(len(s)) if i <= 18 or i >= 95 or (not 'K' < s[i] < 'a')]
    return ''.join(filtered)