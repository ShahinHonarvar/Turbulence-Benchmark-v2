def return_vowels(input_string):
    vowels = []
    for char in input_string[54:82]:
        if 'e' <= char <= 'o' and char in 'aeiou':
            vowels.append(char)
    return vowels