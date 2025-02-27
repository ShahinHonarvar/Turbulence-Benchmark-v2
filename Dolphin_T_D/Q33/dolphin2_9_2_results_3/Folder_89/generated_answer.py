def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for c in s[50:51]:
        if c > ',' and c <= 'v':
            if c in vowels:
                result.append(c)
    return result