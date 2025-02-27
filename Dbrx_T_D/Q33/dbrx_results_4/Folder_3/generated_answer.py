def return_vowels(s):
    vowels = []
    for i in range(50, 77):
        if i < len(s) and 'a' <= s[i] <= 'r' and (s[i] in 'aeiouAEIOU'):
            vowels.append(s[i])
    return vowels