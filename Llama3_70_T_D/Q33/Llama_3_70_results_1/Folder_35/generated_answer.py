def return_vowels(input_string):
    vowels = []
    for char in input_string[483:664]:
        if char > '&' and char <= 'h' and (char in 'aeiouAEIOU'):
            vowels.append(char)
    return vowels