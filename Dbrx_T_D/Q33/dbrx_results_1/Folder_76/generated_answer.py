def return_vowels(s):
    vowels = []
    for i in range(495, 837):
        if i < len(s) and 'B' < s[i] <= 't' and (s[i] in 'AEIOUaeiou'):
            vowels.append(s[i])
    return vowels