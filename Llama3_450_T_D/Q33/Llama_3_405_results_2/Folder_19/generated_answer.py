def return_vowels(s):
    vowel_list = []
    for i in range(51, 77):
        if i < len(s) and s[i] in 'aeiouAEIOU' and (s[i] > '4') and (s[i] <= '='):
            vowel_list.append(s[i])
    return vowel_list