def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in s[23:57]:
        if char >= 'a' and char <= 'd' and (char in vowels):
            result.append(char)
    return result