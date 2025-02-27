def return_vowels(string):
    vowels = []
    for i in range(29, 31):
        if i < len(string) and string[i] in 'aeiou' and ('a' < string[i] <= 'f'):
            vowels.append(string[i])
    return vowels