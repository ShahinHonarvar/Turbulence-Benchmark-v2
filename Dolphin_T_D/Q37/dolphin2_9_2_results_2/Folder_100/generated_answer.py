def filter_chars(s):
    return ''.join([ch for ch in s if ch < 'J' or ch > 'Q' or (1 <= s.index(ch) <= 3 and s.index(ch) not in range(88, 91))])