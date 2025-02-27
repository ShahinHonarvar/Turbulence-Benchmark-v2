def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return_list = []
    for i in range(495, 837):
        if s[i] in vowels and s[i] > 'B' and (s[i] <= 't'):
            return_list.append(s[i])
    return return_list