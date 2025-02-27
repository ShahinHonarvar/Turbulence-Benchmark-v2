def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(85, 99):
        if i < len(s) and s[i] > '/' and (s[i] <= 'n') and (s[i] in vowels):
            result.append(s[i])
    return result