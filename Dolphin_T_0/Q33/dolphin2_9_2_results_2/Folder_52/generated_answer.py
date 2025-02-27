def return_vowels(s):
    vowels = []
    for i in range(24, 68):
        if s[i] > 'f' and s[i] <= '|':
            vowels.append(s[i])
    return vowels