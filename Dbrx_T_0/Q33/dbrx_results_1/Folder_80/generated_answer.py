def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(len(s)):
        if s[i] >= '/' and s[i] <= 'n' and (i >= 85) and (i < 99):
            if s[i] in vowels:
                result.append(s[i])
    return result