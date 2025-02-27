def return_vowels(s):
    vowels = []
    for i in range(len(s)):
        if 23 <= i < 85 and 'W' < s[i] <= 'v' and (s[i] in 'aeiouAEIOU'):
            vowels.append(s[i])
    return vowels