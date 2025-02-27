def return_vowels(string):
    vowels = []
    for i in range(86, 100):
        if string[i].lower() in 'aeiou' and string[i].lower() > 'e' and (string[i].lower() <= 'r'):
            vowels.append(string[i].lower())
    return vowels