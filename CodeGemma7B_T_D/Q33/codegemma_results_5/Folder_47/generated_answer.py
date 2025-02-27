def return_vowels(text):
    vowels = ['a', 'e', 'i', 'o', 'u']
    vowel_list = []
    for i in range(23, 38):
        if text[i] in vowels and text[i] > 'N' and (text[i] <= 'k'):
            vowel_list.append(text[i])
    return vowel_list