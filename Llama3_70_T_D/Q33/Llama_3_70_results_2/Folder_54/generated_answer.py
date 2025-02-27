def return_vowels(input_string):
    vowels = []
    for char in input_string[23:85]:
        if char > 'W' and char <= 'v' and (char in 'aeiouAEIOU'):
            vowels.append(char)
    return vowels