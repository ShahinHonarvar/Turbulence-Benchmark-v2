def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return_list = []
    for i in range(260, 322):
        if s[i] > '%' and s[i] <= 'U':
            if s[i] in vowels:
                return_list.append(s[i])
    return return_list