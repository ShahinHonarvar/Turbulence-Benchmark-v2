def return_vowels(string):
    vowels = []
    for i in range(55, 65):
        if string[i].lower() in 'aeiou' and string[i] > 'Z' and (string[i] <= 'w'):
            vowels.append(string[i])
    return vowels