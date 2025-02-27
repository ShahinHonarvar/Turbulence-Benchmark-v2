def return_vowels(s):
    vowel_list = []
    for i in range(163, 771):
        if ':' < s[i] <= 'E':
            if s[i] in 'AEIOUaeiou':
                vowel_list.append(s[i])
    return vowel_list