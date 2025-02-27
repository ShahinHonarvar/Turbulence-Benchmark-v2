def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    list_vowels = []
    for i in range(37, 57):
        if '*' < s[i] <= 'P':
            if s[i] in vowels:
                list_vowels.append(s[i])
    return list_vowels