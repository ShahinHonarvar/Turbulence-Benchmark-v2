def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in s[56:90]:
        if char.lower() > 'k' and char.lower() <= 'z' and (char.lower() in vowels):
            result.append(char)
    return result