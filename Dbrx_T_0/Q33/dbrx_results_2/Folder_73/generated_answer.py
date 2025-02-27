def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in s[47:89]:
        if char > '@' and char <= 'n' and (char in vowels):
            result.append(char)
    return result