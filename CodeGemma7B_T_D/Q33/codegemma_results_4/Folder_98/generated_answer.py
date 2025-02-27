def return_vowels(strin):
    vowel_list = []
    for i in strin[3:9]:
        if i in 'AEIOUaeiou' and i > 'S' and (i <= 'U'):
            vowel_list.append(i)
    return vowel_list