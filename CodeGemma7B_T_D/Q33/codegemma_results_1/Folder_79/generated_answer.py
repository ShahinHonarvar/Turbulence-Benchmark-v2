def return_vowels(s):
    str_list = s.lower()
    vowels_list = ['a', 'e', 'i', 'o', 'u']
    vowels = []
    for i in range(74, 96):
        if str_list[i] in vowels_list and vowels_list.index(str_list[i]) > vowels_list.index('i') and (vowels_list.index(str_list[i]) <= vowels_list.index('x')):
            vowels.append(str_list[i])
    return vowels