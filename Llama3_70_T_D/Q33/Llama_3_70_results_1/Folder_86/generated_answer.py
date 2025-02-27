def return_vowels(s):
    vowels = []
    for char in s[273:275]:
        if '+' < char <= 'o' and char in 'aeiou':
            vowels.append(char)
    return vowels