def return_vowels(input_string):
    vowels = []
    for char in input_string[770:852]:
        if 'B' < char <= 'i' and char in 'aeiouAEIOU':
            vowels.append(char)
    return vowels