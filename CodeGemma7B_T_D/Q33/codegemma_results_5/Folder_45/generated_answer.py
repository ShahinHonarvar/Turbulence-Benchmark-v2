def return_vowels(word):
    vowels = 'aeiouAEIOU'
    vowel_list = []
    for i in range(43, 70):
        if word[i] in vowels and word[i] > '*' and (word[i] <= 'b'):
            vowel_list.append(word[i])
    return vowel_list