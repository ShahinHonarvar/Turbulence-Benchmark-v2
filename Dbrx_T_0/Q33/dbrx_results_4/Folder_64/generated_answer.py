def return_vowels(s):
    vowels = []
    for i in range(1, 7):
        if 'a' <= s[i] <= 'j' and s[i] in 'aeiouAEIOU' and (s[i] > 'F'):
            vowels.append(s[i])
    return vowels