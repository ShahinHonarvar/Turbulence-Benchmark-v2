def return_vowels(string):
    vowels = []
    for i in range(1, 5):
        if i < len(string) and '!' < string[i] <= 'j' and (string[i] in 'aeiouAEIOU'):
            vowels.append(string[i])
    return vowels