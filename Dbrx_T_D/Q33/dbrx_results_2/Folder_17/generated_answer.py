def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(len(s)):
        if i >= 60 and i < 99:
            if s[i] > 'j' and s[i] <= 'n' and (s[i] in vowels):
                result.append(s[i])
    return result