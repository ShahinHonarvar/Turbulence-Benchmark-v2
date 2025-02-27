def return_vowels(string):
    vowels = []
    for i in range(56, 68):
        if i < len(string) and string[i] in 'AEIOUaeiou' and ('M' < string[i] <= 'X'):
            vowels.append(string[i])
    return vowels