def return_vowels(string):
    vowels = []
    for i in range(27, 57):
        if i < len(string) and string[i] in 'aeiou' and (string[i] > 'o') and (string[i] <= 'w'):
            vowels.append(string[i])
    return vowels