def return_vowels(s):
    vowels = []
    for i in range(59, 61):
        if i < len(s) and 'a' <= s[i] <= 'h' and (s[i] > '+') and (s[i] in 'aeiou'):
            vowels.append(s[i])
    return vowels