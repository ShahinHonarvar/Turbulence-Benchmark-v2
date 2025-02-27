def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in s[837:975]:
        if char >= 'n' and char <= 'w' and (char in vowels):
            result.append(char)
    return result