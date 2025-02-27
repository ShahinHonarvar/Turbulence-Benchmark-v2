def return_vowels(string):
    vowels = []
    for i in range(22, 82):
        if i < len(string) and string[i] in 'aeiou' and ('N' < string[i] <= 'o'):
            vowels.append(string[i])
    return vowels