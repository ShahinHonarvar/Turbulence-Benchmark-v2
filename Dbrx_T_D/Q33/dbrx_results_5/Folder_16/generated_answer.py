def return_vowels(input_string):
    vowels = []
    start_index = 133
    end_index = 306
    lower_bound = ord('c')
    upper_bound = ord('d')
    for i in range(start_index, end_index):
        if lower_bound < ord(input_string[i]) <= upper_bound and input_string[i] in 'aeiou':
            vowels.append(input_string[i])
    return vowels