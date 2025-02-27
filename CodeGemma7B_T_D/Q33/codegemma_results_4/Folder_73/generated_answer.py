def return_vowels(string):
    vowels = list('aeiouAEIOU')
    result = []
    for letter in string[47:89]:
        if letter in vowels and letter > '@' and (letter <= 'n'):
            result.append(letter)
    return result