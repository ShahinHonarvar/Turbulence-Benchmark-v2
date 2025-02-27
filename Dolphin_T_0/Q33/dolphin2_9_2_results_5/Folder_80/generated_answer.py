def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return_list = []
    for i in range(85, 99):
        if '/' < s[i] <= 'n' and s[i] in vowels:
            return_list.append(s[i])
    return return_list