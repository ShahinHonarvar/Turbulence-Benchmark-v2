def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in s[495:837]:
        if char.lower() > 'b' and char.lower() <= 't' and (char.lower() in vowels):
            result.append(char)
    return result