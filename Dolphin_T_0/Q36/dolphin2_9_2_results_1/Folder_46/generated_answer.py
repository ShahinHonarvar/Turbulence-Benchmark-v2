def filter_chars(s):
    chars_to_remove = [s[i] for i in range(20, 70) if 'A' < s[i] < 'C']
    result = ''
    for c in s:
        if c not in chars_to_remove:
            result += c
    return result