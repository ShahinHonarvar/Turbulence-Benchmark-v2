def return_vowels(string):
    vowels = 'aeiouAEIOU'
    result = []
    for i, letter in enumerate(string):
        if i >= 273 and i < 275 and (letter in vowels):
            if letter > '+' and letter <= 'o':
                result.append(letter)
    return result