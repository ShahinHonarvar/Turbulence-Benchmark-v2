def return_vowels(s):
    vowel_list = []
    vowels = ['a', 'e', 'i', 'o', 'u']
    for i in range(45, 76):
        if i < len(s) and s[i] > 'b' and (s[i] <= 'z') and (s[i] in vowels):
            vowel_list.append(s[i])
    return vowel_list