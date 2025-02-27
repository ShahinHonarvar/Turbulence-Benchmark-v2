def return_vowels(s):
    vowels = []
    for i in range(21, 59):
        if i < len(s) and s[i] in 'aeiou' and ('/' < s[i] <= 'a'):
            vowels.append(s[i])
    return vowels