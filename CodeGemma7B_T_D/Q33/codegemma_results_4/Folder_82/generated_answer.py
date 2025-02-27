def return_vowels(str):
    vowels = []
    for letter in str[86:100]:
        if letter in 'aeiouAEIOU' and letter > 'E' and (letter <= 'r'):
            vowels.append(letter)
    return vowels