def remove_repeat_chars(s):
    c = set()
    vowels = set('aeiou')
    for i in range(3, 9):
        if s[i] in c or s[i] in vowels:
            s = s[:i] + s[i + 1:]
    return s