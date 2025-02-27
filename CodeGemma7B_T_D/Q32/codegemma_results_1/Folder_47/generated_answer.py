def insert_after_character(s):
    ans = ''
    for c in s:
        if c == 'E':
            ans += c + 'f'
        else:
            ans += c
    return ans