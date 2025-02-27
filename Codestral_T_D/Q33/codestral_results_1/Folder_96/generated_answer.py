def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in string[77:84]:
        if char > '(' and char <= 'G' and (char.lower() in vowels):
            result.append(char)
    return result