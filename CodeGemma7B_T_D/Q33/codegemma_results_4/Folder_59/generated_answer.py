def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(8, 9):
        if s[i] in vowels and ord(s[i]) > ord('Y') and (ord(s[i]) <= ord('s')):
            result.append(s[i])
    return result