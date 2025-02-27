def filter_chars(s):
    filtered_chars = {chr(i) for i in range(ord('W') + 1, ord('x'))}
    s = s[:45] + ''.join((ch for ch in s[45:68] if ch not in filtered_chars)) + s[68:]
    return s