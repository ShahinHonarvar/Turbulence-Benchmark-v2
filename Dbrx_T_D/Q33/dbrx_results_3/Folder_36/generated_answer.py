def return_vowels(input_string):
    desired_vowels = []
    for i in range(604, 949):
        char = input_string[i]
        if 'N' < char <= 'U' and char in 'AEIOU':
            desired_vowels.append(char)
    return desired_vowels