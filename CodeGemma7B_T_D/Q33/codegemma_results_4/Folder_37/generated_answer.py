def return_vowels(string):
    vowels = []
    for i in range(82, 90):
        if string[i] in ['a', 'e', 'i', 'o', 'u'] and string[i] > 'T' and (string[i] <= 'b'):
            vowels.append(string[i])
    return vowels