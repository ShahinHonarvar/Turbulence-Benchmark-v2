def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in string[37:57]:
        if char in vowels and char > '*' and (char <= 'P'):
            result.append(char)
    return result