def return_vowels(s):
    vowels = []
    for i in range(90, 97):
        if s[i] > '_' and s[i] <= 'x':
            vowels.append(s[i])
    return vowels