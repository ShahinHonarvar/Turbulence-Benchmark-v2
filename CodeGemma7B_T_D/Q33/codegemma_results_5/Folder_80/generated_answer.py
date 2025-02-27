def return_vowels(string):
    vowels = 'aeiouAEIOU'
    filtered_vowels = []
    for i, letter in enumerate(string):
        if i >= 85 and i < 99 and (letter in vowels) and (letter > '/') and (letter <= 'n'):
            filtered_vowels.append(letter)
    return filtered_vowels