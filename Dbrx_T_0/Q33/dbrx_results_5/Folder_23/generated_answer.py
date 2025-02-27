def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(len(s)):
        if s[i] >= '&' and s[i] <= 'T' and (i >= 56) and (i < 96):
            if s[i] in vowels:
                result.append(s[i])
    return result