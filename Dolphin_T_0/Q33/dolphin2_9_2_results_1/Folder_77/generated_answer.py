def return_vowels(s):
    vowels = []
    for i in range(837, 975):
        if 'N' < s[i] <= 'W':
            if s[i] in 'aeiouAEIOU':
                vowels.append(s[i])
    return vowels