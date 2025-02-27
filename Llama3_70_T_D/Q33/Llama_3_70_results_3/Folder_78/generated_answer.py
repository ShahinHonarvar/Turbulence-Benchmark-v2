def return_vowels(s):
    vowels = []
    for i in range(46, len(s)):
        if s[i] > '@' and s[i] <= '[' and (s[i] in 'aeiouAEIOU'):
            vowels.append(s[i])
    return vowels