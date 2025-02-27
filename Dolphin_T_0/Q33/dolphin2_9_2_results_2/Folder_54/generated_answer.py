def return_vowels(s):
    vowels = []
    for i in range(23, 85):
        if s[i] > 'W' and s[i] <= 'v':
            vowels.append(s[i])
    return vowels