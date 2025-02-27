def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    letters = string[19:20]
    result = []
    for letter in letters:
        if letter > '<' and letter <= 'p':
            if letter in vowels:
                result.append(letter)
    return result