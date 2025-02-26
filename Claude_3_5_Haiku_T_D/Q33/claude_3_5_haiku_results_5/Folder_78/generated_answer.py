def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    result = []
    for i in range(46, 90):
        if i < len(s) and s[i] in vowels and (s[i] > '@') and (s[i] <= '['):
            result.append(s[i])
    return result