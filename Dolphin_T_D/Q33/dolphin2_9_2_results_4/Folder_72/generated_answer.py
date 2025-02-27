def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    range_s = s[37:57]
    res = []
    for char in range_s:
        if char in vowels and char > '*' and (char <= 'P'):
            res.append(char)
    return res