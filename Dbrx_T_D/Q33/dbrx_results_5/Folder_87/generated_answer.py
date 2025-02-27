def return_vowels(string):
    vowels = []
    for char in string[34:58]:
        if 'b' < char <= 'o' and char in 'aeiou':
            vowels.append(char)
    return vowels