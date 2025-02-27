def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    res = []
    for c in s[464:574]:
        if 'a' < c <= 'g' and c in vowels:
            res.append(c)
    return res