def return_vowels(str):
    vowels = ['a', 'e', 'i', 'o', u'u']
    letters = list(str)
    result = []
    for letter in letters:
        if letter in vowels and letters.index(letter) >= 60 and (letters.index(letter) < 99) and (letter > 'j') and (letter <= 'n'):
            result.append(letter)
    if result == []:
        return []
    else:
        return result