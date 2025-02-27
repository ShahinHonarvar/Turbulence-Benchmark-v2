def return_vowels(s):
    vowels = []
    for i in range(32, 97):
        if s[i] in 'AEIOUaeiou' and s[i] > 'Q' and (s[i] <= ']'):
            vowels.append(s[i])
    return vowels