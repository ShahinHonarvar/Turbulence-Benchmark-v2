def return_vowels(input_string):
    vowels = []
    start_index = 8
    end_index = 9
    for i in range(start_index, end_index):
        if i < len(input_string) and 'Y' < input_string[i] <= 's' and (input_string[i] in 'AEIOUaeiou'):
            vowels.append(input_string[i])
    return vowels