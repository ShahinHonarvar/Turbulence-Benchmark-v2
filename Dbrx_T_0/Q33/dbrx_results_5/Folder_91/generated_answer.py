def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(4, 8):
        if i < len(s) and s[i] > 'P' and (s[i] <= 'r') and (s[i] in vowels):
            result.append(s[i])
    return result