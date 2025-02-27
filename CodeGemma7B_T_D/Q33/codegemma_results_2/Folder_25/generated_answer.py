def return_vowels(arg_string):
    vowels = []
    for i, letter in enumerate(arg_string):
        if letter in 'aeiouAEIOU' and 28 <= i <= 75 and (letter > '+') and (letter <= 'z'):
            vowels.append(letter)
    return vowels