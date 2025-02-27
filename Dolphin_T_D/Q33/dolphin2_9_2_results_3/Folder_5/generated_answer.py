def return_vowels(s):
    v = ['a', 'e', 'i', 'o', 'u']
    return_list = []
    for i in range(44, 95):
        if 6 < ord(s[i]) < ord('<'):
            if s[i] in v:
                return_list.append(s[i])
    return return_list