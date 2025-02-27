def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for c in s[34:58]:
        if 'b' < c <= 'o' and c in vowels:
            result.append(c)
    return result