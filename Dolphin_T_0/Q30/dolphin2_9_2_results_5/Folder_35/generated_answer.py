def insert_before_character(s):
    ans = ''
    for i in s:
        if i == '9':
            ans += 'M'
            ans += i
        else:
            ans += i
    return ans