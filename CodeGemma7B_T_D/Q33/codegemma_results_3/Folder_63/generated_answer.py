def return_vowels(arg):
    valid_letters = {'a', 'e', 'i', 'o', 'u'}
    result = []
    for i in range(34, 69):
        letter = arg[i].lower()
        if letter in valid_letters and letter > '_' and (letter <= 'o'):
            result.append(letter)
    return result