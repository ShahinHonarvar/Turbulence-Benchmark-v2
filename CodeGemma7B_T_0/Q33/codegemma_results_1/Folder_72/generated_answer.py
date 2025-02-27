def return_vowels(string):
    vowels = []
    for i in range(37, 57):
        if string[i].lower() in 'aeiou' and string[i] > '*' and (string[i] <= 'p'):
            vowels.append(string[i])
    return vowels