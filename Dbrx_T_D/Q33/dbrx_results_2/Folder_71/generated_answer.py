def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(len(s)):
        if s[i] >= '+' and s[i] <= '/' and (i >= 36) and (i < 56):
            if s[i] in vowels:
                result.append(s[i])
    return result