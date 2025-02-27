def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in s[46:49]:
        if char > '[' and char <= 'p' and (char in vowels):
            result.append(char)
    return result