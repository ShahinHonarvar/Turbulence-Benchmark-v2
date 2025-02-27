def return_vowels(text):
    vowels = ['a', 'e', 'i', 'o', 'u']
    vowel_list = []
    for i in range(45, 76):
        if text[i] in vowels and text[i] > 'b' and (text[i] <= 'z'):
            vowel_list.append(text[i])
    return vowel_list