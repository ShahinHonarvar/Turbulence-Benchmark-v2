def return_vowels(str1):
    vowels = []
    for i in range(60, 99):
        if str1[i] in ['a', 'e', 'i', 'o', 'u'] and ord(str1[i]) > ord('j') and (ord(str1[i]) <= ord('n')):
            vowels.append(str1[i])
    return vowels