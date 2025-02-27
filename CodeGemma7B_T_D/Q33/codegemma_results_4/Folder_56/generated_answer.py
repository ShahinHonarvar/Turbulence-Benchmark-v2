def return_vowels(str):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(15, 86):
        if str[i] in vowels and ord(str[i]) > ord('@') and (ord(str[i]) <= ord('~')):
            result.append(str[i])
    return result