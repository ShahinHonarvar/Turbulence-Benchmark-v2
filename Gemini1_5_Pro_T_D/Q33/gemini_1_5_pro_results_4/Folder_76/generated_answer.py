def return_vowels(string):
    vowels = []
    for i in range(495, 837):
        if i < len(string) and string[i] in 'aeiouAEIOU' and (string[i] > 'B') and (string[i] <= 't'):
            vowels.append(string[i])
    return vowels