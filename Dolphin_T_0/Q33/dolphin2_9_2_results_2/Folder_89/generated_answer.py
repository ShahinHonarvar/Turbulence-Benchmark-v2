def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    res = []
    for char in s[50:51]:
        if vowels.count(char) > 0 and ',' < char <= 'v':
            res.append(char)
    return res