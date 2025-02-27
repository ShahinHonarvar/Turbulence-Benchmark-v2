def return_vowels(s):
    vowels = ['A', 'E', 'I', 'O', 'U']
    res = []
    for char in s[10:82]:
        if '$' < char <= '@' and char in vowels:
            res.append(char)
    return res