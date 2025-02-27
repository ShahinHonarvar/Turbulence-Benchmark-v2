def return_vowels(input_string):
    vowels = []
    for i in range(50, 51):
        char = input_string[i]
        if 'a' <= char <= 'v' and char in 'aeiou':
            vowels.append(char)
    return vowels