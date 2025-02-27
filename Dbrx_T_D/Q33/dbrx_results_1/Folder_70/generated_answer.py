def return_vowels(s):
    vowels = []
    for i in range(len(s)):
        if i >= 171 and i < 402 and ('I' < s[i] <= 'k') and (s[i] in 'aeiouAEIOU'):
            vowels.append(s[i])
    return vowels