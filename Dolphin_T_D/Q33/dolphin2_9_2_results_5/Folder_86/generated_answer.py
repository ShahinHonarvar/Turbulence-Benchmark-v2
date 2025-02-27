def return_vowels(string):
    vowels = []
    for char in string[273:275]:
        if 'a' <= char <= 'o' and char in 'aeiou':
            vowels.append(char)
    return vowels