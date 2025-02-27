def return_vowels(word):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i, letter in enumerate(word):
        if i >= 60 and i < 99 and (letter in vowels) and (letter > 'j') and (letter <= 'n'):
            result.append(letter)
    return result