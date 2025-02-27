from string import ascii_lowercase

def return_vowels(text):
    vowels = []
    for i in range(86, 99):
        if text[i] in ascii_lowercase and text[i] > 'E' and (text[i] <= 'r'):
            vowels.append(text[i])
    return vowels