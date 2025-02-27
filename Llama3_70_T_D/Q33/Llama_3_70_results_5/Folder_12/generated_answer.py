def return_vowels(s):
    vowels = []
    for i in range(13, 37):
        if s[i] > 'Z' and s[i] <= '}' and (s[i] in 'AEIOUaeiou'):
            vowels.append(s[i])
    return vowels