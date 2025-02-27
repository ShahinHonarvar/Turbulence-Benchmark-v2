def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in s[55:65]:
        if char > 'Z' and char <= 'w' and (char.lower() in vowels):
            result.append(char)
    return result