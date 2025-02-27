def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in string[1:4]:
        if char.lower() > 'c' and char.lower() <= 'i' and (char.lower() in vowels):
            result.append(char)
    return result