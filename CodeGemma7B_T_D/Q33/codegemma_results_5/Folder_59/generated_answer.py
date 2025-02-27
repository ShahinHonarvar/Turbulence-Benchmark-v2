def return_vowels(word):
    vowels = []
    for i in range(8, 9):
        if word[i] in 'aeiouAEIOU' and word[i] > 'Y' and (word[i] <= 's'):
            vowels.append(word[i])
    return vowels