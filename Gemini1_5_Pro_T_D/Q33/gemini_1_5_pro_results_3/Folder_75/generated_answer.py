def return_vowels(string):
    vowels = []
    for i in range(20, 41):
        if i < len(string) and string[i] in 'AEIOU' and (string[i] > 'K') and (string[i] <= 'Z'):
            vowels.append(string[i])
    return vowels