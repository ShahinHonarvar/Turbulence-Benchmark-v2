def return_vowels(string):
    vowels = list()
    for i in range(32, 61):
        if string[i] in 'AEIOUaeiou':
            vowels.append(string[i])
    return vowels