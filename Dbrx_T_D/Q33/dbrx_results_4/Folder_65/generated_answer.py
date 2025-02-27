def return_vowels(input_string):
    vowels = []
    for char in input_string[71:88]:
        if 'i' <= char <= 'p' and char in 'aeiouAEIOU':
            vowels.append(char)
    return vowels