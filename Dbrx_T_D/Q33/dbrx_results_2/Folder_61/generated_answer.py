def return_vowels(string):
    vowels = []
    for char in string[1:4]:
        if 'C' < char <= 'I' and char in 'AEIOUaeiou':
            vowels.append(char)
    return vowels