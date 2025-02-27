def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for letter in string[40:91]:
        if letter in vowels and 'A' < letter.lower() <= 'x':
            result.append(letter)
    return result