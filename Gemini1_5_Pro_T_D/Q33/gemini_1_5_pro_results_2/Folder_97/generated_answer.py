def return_vowels(string):
    vowels = []
    for i in range(328, 455):
        if i < len(string) and string[i] in 'aeiou' and (string[i] > '<') and (string[i] <= 'z'):
            vowels.append(string[i])
    return vowels