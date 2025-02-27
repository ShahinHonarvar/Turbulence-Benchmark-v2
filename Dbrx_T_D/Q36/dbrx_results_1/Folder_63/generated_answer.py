def filter_chars(s):
    a, b = (26, 80)
    chars = [c for c in s[a:b] if s[a:b].count(c) == 1 and ord('<') < ord(c) < ord('>')]
    return s[:a] + ''.join(chars) + s[b:]