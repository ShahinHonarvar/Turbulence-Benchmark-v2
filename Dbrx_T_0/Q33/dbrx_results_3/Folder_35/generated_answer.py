def return_vowels(s):
    vowels = []
    for i in range(len(s)):
        if i >= 483 and i < 664:
            if s[i] > '&' and s[i] <= 'h' and (s[i] in 'aeiouAEIOU'):
                vowels.append(s[i])
    return vowels