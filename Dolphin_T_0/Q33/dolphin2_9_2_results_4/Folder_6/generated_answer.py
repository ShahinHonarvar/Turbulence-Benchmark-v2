def return_vowels(s):
    vowels = ['U', 'u', 'O', 'o', 'I', 'i']
    return_list = []
    for i in range(20, 34):
        if vowels.__contains__(s[i]):
            return_list.append(s[i])
    return return_list