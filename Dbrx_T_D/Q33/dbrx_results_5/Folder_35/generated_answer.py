def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(len(s)):
        if i >= 483 and i < 664 and (s[i] > '&') and (s[i] <= 'h'):
            if s[i] in vowels:
                result.append(s[i])
    return result