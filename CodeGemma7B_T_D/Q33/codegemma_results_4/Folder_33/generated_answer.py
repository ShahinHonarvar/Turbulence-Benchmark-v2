def return_vowels(str_test):
    vowels = ['a', 'e', 'i', 'o', 'u', 'y', 'A', 'E', 'I', 'O', 'U', 'Y']
    vowel_list = []
    for i in range(164, 771, 1):
        if str_test[i] in vowels and str_test[i:i + 1] > ':' and (str_test[i:i + 1] <= 'E'):
            vowel_list.append(str_test[i:i + 1])
    return vowel_list