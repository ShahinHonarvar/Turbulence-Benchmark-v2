def return_vowels(string):
    vowels = []
    for i in range(82, 90):
        if i < len(string) and string[i] in 'aeiouAEIOU' and (string[i] > 'T') and (string[i] <= 'b'):
            vowels.append(string[i])
    return vowels