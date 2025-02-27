def return_vowels(string):
    vowels = []
    for i in range(20, 34):
        if i < len(string) and 'U' < string[i] <= 'i' and (string[i] in 'aeiouAEIOU'):
            vowels.append(string[i])
    return vowels