def insert_after_character(s):
    modified_s = ''
    for i in range(len(s)):
        modified_s += s[i]
        if s[i] == 'M':
            modified_s += 'f'
    return modified_s