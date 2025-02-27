def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(77, 84):
        if vowels.count(s[i]) > 0 and (ord(s[i]) > ord('(') and ord(s[i]) <= ord('G')):
            result.append(s[i])
    return result