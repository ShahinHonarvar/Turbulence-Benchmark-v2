def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for c in s[23:57]:
        if c > '0' and c <= 'd' and (c in vowels):
            result.append(c)
    return result