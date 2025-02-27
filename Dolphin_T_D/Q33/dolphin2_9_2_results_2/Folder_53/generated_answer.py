def return_vowels(input_string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    vowels_in_range = []
    for i in range(27, 57):
        if input_string[i] > 'o' and input_string[i] <= 'w' and (input_string[i] in vowels):
            vowels_in_range.append(input_string[i])
    return vowels_in_range