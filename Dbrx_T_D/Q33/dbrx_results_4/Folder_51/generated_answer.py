def return_vowels(input_string):
    vowels = []
    for char in input_string[56:68]:
        if char.isalpha() and 'M' < char <= 'X' and (char in 'AEIOU'):
            vowels.append(char)
    return vowels