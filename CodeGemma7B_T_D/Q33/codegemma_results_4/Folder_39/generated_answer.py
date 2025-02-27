def return_vowels(text):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for index, letter in enumerate(text):
        if index >= 32 and index < 97 and (letter in vowels) and (letter > 'Q') and (letter <= ']'):
            result.append(letter)
    return result