def return_vowels(string):
    vowels = []
    for i in range(1, 4):
        if string[i] in 'aeiouAEIOU' and '!' < string[i] <= 'j':
            vowels.append(string[i])
    return vowels