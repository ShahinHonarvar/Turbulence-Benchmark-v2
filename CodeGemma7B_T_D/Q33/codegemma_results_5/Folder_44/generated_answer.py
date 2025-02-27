def return_vowels(vowels):
    vowel = 'aeiouAEIOU'
    vowels_list = []
    for i in vowels[46:49]:
        if i in vowel and i > '[' and (i <= 'p'):
            vowels_list.append(i)
    return vowels_list