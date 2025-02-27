def return_vowels(string):
    vowels = []
    for i in range(36, 56):
        if string[i] > '+' and string[i] <= '/' and (string[i].lower() in 'aeiou'):
            vowels.append(string[i])
    return vowels