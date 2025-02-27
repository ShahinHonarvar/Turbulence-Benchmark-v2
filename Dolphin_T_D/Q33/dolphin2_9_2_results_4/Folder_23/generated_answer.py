def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in s[56:96]:
        if char >= '&' and char <= 'T':
            if char in vowels:
                result.append(char)
    return result