def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for letter in string[32:61]:
        if letter in vowels and letter > '?' and (letter <= 'P'):
            result.append(letter)
    return result