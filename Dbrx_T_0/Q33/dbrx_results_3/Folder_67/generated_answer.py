def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(len(s)):
        if s[i] > '/' and s[i] <= 'a' and (i >= 21) and (i < 59):
            if s[i] in vowels:
                result.append(s[i])
    return result