def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(20, 34):
        if i < len(s) and s[i] > 'U' and (s[i] <= 'i') and (s[i] in vowels):
            result.append(s[i])
    return result