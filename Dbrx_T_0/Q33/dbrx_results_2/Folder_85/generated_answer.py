def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in s[55:65]:
        if char.lower() > 'z' and char.lower() <= 'w' and (char.lower() in vowels):
            result.append(char)
    return result