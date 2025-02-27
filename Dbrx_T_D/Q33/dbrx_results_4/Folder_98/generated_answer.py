def return_vowels(s):
    vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(3, 9):
        if i >= 3 and i < 9 and (vowels.index(s[i]) >= vowels.index('S')) and (vowels.index(s[i]) <= vowels.index('U')):
            result.append(s[i])
    return result