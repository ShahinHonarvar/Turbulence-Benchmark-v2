def return_vowels(string):
    vowels = []
    for i in range(21, 59):
        if i < len(string) and string[i] in 'aeiou' and ('/' < string[i] <= 'a'):
            vowels.append(string[i])
    return vowels