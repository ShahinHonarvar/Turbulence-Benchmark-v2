def return_vowels(input_string):
    vowels = []
    for i in range(len(input_string)):
        if i >= 50 and i < 77:
            if input_string[i] > '#' and input_string[i] <= 'r':
                if input_string[i] in 'aeiouAEIOU':
                    vowels.append(input_string[i])
    return vowels