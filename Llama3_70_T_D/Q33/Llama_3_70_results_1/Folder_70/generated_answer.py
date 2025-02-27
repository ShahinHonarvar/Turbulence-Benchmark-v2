def return_vowels(input_string):
    vowels = []
    for char in input_string[171:402]:
        if 'I' < char <= 'k' and char in 'aeiouAEIOU':
            vowels.append(char)
    return vowels