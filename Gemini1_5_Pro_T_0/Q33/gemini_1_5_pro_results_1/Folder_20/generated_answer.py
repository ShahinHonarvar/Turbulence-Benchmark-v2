def return_vowels(string):
    vowels = []
    for i in range(59, 61):
        if i < len(string) and string[i] in 'aeiouAEIOU' and ('+' < string[i] <= 'h'):
            vowels.append(string[i])
    return vowels