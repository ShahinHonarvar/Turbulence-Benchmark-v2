def return_vowels(string):
    vowels = []
    for i in range(171, 402):
        if string[i] in 'aeiouAEIOU' and string[i] > 'I' and (string[i] <= 'k'):
            vowels.append(string[i])
    return vowels