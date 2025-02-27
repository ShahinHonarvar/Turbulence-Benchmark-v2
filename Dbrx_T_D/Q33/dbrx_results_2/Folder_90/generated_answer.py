def return_vowels(input_string):
    vowels = []
    for i in range(142, 145):
        char = input_string[i]
        if 'e' <= char <= 'o' and char > '4':
            vowels.append(char)
    return vowels