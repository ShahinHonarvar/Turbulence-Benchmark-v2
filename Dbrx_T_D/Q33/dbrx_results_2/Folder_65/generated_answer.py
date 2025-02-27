def return_vowels(string):
    vowels = []
    for char in string[70:87]:
        if '9' < char <= 'P' and char in 'AEIOU':
            vowels.append(char)
    return vowels