def insert_after_character(s):
    new_s = ''
    for i in range(len(s)):
        new_s = new_s + s[i]
        if s[i] == 'P':
            new_s = new_s + 'V'
    return new_s