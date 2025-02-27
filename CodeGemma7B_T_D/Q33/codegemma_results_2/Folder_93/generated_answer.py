def return_vowels(str_to_check):
    vowels = ['a', 'e', 'i', 'o', 'u']
    vowel_list = []
    for i in range(54, 82):
        if str_to_check[i] in vowels and str_to_check[i] >= '=' and (str_to_check[i] <= '@'):
            vowel_list.append(str_to_check[i])
    if vowel_list == []:
        return []
    else:
        return vowel_list