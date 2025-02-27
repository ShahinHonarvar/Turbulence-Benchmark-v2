def return_vowels(s):
    vowels = []
    for i in range(len(s)):
        if i >= 171 and i < 402:
            if s[i] > 'I' and s[i] <= 'k' and (s[i] in 'aeiouAEIOU'):
                vowels.append(s[i])
    return vowels