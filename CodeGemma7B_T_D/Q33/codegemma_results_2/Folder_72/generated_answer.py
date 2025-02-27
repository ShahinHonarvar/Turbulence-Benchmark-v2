def return_vowels(string):
    vowels = []
    for i in range(37, 57):
        if string[i] in 'AEIOUaeiou' and string[i] > '*' and (string[i] <= 'P'):
            vowels.append(string[i])
    return vowels or []