def return_vowels(word):
    vowels = []
    for letter in word[22:82]:
        if letter in ['a', 'e', 'i', 'o', 'u'] and letter > 'N' and (letter <= 'o'):
            vowels.append(letter)
    return vowels