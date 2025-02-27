def return_vowels(s):
    vowels = []
    for i in range(len(s)):
        if i >= 22 and i < 82:
            if s[i] > 'N' and s[i] <= 'o' and (s[i] in 'AEIOUaeiou'):
                vowels.append(s[i])
    return vowels