def return_vowels(input_string):
    vowels = []
    for char in input_string[37:57]:
        if char.lower() in 'aeiou' and '*' < char <= 'P':
            vowels.append(char)
    return vowels