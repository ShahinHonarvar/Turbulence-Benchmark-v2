def return_vowels(string):
    vowels = []
    for i in range(56, 90):
        if string[i].lower() in 'aeiou' and string[i] > 'K' and (string[i] <= 'z'):
            vowels.append(string[i])
    return vowels