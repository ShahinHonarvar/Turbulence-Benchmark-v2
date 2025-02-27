def return_vowels(string):
    vowels = []
    for i in range(40, 91):
        if string[i].lower() in 'aeiou' and string[i].lower() > 'a' and (string[i].lower() <= 'x'):
            vowels.append(string[i].lower())
    return vowels