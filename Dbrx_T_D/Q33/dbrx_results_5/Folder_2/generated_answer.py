def return_vowels(input_string):
    vowels = []
    for char in input_string[170:645]:
        if 'E' < char <= '~' and char.lower() in 'aeiou':
            vowels.append(char)
    return vowels