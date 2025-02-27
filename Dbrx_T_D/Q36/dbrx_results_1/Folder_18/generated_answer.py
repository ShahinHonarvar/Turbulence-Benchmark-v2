def filter_chars(s):
    return ''.join((char for char in s[587:648] if s[587:648].index(char) < s[587:648].index('c') - s[587:648].index(',') - 1)) + s[:587] + s[648:]