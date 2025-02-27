def filter_chars(s):
    if len(s) < 20:
        return s
    chars_to_remove = set()
    for i in range(20, min(80, len(s))):
        if '!' <= s[i] <= 'T':
            chars_to_remove.add(s[i])
    result = [char for char in s if char not in chars_to_remove]
    return ''.join(result)