def return_vowels(str):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(133, 306):
        if str[i] in vowels and ord(str[i]) > ord('c') and (ord(str[i]) <= ord('d')):
            result.append(str[i])
    return result