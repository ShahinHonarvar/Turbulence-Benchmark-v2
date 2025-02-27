def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(len(s)):
        if s[i] >= '<' and s[i] <= 'z' and (i >= 328) and (i < 455):
            if s[i] in vowels:
                result.append(s[i])
    return result