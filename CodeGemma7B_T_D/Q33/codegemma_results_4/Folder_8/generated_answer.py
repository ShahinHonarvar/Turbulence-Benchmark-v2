def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return_list = []
    for i in range(64, 82):
        if s[i] in vowels and s[i] > 'p' and (s[i] <= 'z'):
            return_list.append(s[i])
    return return_list