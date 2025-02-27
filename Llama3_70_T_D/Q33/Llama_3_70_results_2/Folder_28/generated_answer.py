def return_vowels(s):
    vowels = []
    for i in range(41, 50):
        if len(s) > i and 'W' < s[i] <= '[' and (s[i] in 'AEIOUaeiou'):
            vowels.append(s[i])
    return vowels