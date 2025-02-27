def return_vowels(string):
    vowels = []
    for i in range(1, min(4, len(string))):
        if string[i] in 'AEIOUaeiou' and 'C' < string[i] <= 'I':
            vowels.append(string[i])
    return vowels