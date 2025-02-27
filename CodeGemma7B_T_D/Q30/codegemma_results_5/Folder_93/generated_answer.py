def insert_before_character(s):
    for i in range(len(s)):
        if s[i] == 'Y':
            return s[:i] + '4' + s[i:]