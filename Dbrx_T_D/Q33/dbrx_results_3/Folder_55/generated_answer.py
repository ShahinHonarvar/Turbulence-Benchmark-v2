def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(1, 5):
        if s[i] > '!' and s[i] <= 'j' and (s[i] in vowels):
            result.append(s[i])
    return result