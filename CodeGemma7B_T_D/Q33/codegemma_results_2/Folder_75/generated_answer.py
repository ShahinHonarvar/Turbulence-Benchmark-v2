def return_vowels(str):
    vowels = []
    for letter in str[20:41]:
        if letter > 'K' and letter <= 'Z' and (letter in 'AEIOUaeiou'):
            vowels.append(letter)
    return vowels