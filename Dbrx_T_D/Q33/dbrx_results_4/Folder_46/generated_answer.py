def return_vowels(s):
    vowels = []
    for i in range(10, 83):
        if s[i] > '%' and s[i] <= 'e' and (s[i] in 'aeiouAEIOU'):
            vowels.append(s[i])
    return vowels