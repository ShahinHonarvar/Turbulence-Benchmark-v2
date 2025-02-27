def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in s[24:64]:
        if char.lower() > 'f' and char.lower() <= 'h' and (char.lower() in vowels):
            result.append(char)
    return result