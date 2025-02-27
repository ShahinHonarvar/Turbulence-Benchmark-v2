def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in s[56:68]:
        if char > 'M' and char <= 'X' and (char in vowels):
            result.append(char)
    return result