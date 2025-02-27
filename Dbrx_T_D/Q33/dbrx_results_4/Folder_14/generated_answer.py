def return_vowels(s):
    vowels = []
    for i in range(len(s)):
        if 57 <= ord(s[i]) <= 79 and 49 < i <= 60 and (s[i] in 'AEIOUaeiou'):
            vowels.append(s[i])
    return vowels