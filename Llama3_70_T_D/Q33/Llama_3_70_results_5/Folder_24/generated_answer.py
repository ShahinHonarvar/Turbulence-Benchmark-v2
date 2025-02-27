def return_vowels(s):
    vowels = [s[i] for i in range(23, 57) if s[i] > '0' and s[i] <= 'd' and (s[i] in 'aeiouAEIOU')]
    return vowels