def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(len(s)):
        if i >= 46 and i < 49 and (s[i] > '[') and (s[i] <= 'p') and (s[i] in vowels):
            result.append(s[i])
    return result