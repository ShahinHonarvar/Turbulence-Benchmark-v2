def return_vowels(string):
    vowels = []
    for i in range(90, 97):
        if i >= len(string):
            break
        if string[i] in 'aeiouAEIOU' and string[i] > '_' and (string[i] <= 'x'):
            vowels.append(string[i])
    return vowels