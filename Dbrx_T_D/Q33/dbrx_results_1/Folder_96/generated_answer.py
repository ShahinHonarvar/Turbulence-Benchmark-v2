def return_vowels(string):
    vowel_list = []
    for char in string[77:84]:
        if 'a' <= char <= 'G' and char in 'aeiouAEIOU':
            vowel_list.append(char)
    return vowel_list