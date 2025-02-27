def insert_after_character(s):
    for i in range(len(s)):
        if s[i] == 'A':
            s = s[:i + 1] + 'H' + s[i + 1:]
    return s