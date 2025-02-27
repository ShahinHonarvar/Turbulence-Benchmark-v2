def return_vowels(input_string):
    vowels = []
    for char in input_string[47:89]:
        if char > '@' and char <= 'n' and (char in 'aeiouAEIOU'):
            vowels.append(char)
    return vowels