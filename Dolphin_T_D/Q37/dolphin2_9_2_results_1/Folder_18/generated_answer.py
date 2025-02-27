def filter_chars(s):
    chars_to_remove = [s[i] for i in range(770, 971) if '-'.find(s[i]) >= 0 and '-'.find(s[i]) <= 3]
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s