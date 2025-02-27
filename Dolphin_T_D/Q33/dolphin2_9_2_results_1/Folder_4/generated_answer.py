def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for c in s[40:91]:
        if 'a' < c <= 'x' and c in vowels:
            result.append(c)
    return result