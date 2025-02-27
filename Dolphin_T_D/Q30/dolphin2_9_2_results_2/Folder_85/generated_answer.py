def insert_before_character(s):
    new_s = []
    for i in range(len(s)):
        if s[i] == 'o':
            new_s.append('a' + s[i])
        else:
            new_s.append(s[i])
    result = ''.join(new_s)
    return result