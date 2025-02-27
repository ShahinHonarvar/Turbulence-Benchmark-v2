def return_vowels(input_string):
    vowels = []
    for char in input_string[20:34]:
        if 'U' < char <= 'i' and char in 'aeiou':
            vowels.append(char)
    return vowels