def return_vowels(s):
    vowels = []
    for i in range(70, 76):
        if s[i] > '2' and s[i] <= ':':
            vowels.append(s[i])
    return vowels