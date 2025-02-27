def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in s[40:91]:
        if char.lower() > 'a' and char.lower() <= 'x' and (char.lower() in vowels):
            result.append(char)
    return result