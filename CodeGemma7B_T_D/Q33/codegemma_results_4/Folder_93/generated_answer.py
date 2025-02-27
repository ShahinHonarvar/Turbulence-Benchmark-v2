def return_vowels(string):
    vowels = 'aeiouAEIOU'
    vowels_in_range = []
    for letter in string[54:82]:
        if letter in vowels and letter >= '=' and (letter <= '@'):
            vowels_in_range.append(letter)
    return vowels_in_range