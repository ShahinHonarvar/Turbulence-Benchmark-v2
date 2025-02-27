def return_vowels(string):
    vowels = []
    for i in range(13, 37):
        if i < len(string) and 'Z' < string[i] <= '}' and (string[i] in 'AEIOUaeiou'):
            vowels.append(string[i])
    return vowels