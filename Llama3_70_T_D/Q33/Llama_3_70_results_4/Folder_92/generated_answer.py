def return_vowels(input_string):
    vowels = [char for char in input_string[3:8] if 'a' < char <= 'D' and char in 'aeiouAEIOU']
    return vowels