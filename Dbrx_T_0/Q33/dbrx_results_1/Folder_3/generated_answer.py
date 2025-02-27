def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(len(s)):
        if s[i] >= '#' and s[i] <= 'r' and (i >= 50) and (i < 77):
            if s[i] in vowels:
                result.append(s[i])
    return result