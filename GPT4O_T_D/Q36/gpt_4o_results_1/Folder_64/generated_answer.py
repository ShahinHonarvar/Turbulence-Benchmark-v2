def filter_chars(s):
    filtered_chars = [c for c in s if all((c != s[i] for i in range(2, 7) if '3' < s[i] < '^'))]
    return ''.join(filtered_chars)