def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in s[63:79]:
        if char.lower() > 'd' and char.lower() <= 'y' and (char.lower() in vowels):
            result.append(char)
    return result