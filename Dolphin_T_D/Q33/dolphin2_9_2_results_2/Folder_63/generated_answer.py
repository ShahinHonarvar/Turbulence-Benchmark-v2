def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for c in s[34:69]:
        if '_' < c <= 'o' and c in vowels:
            result.append(c)
    return result