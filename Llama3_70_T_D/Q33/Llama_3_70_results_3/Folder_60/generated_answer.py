def return_vowels(s):
    vowels = [s[i] for i in range(24, 59) if s[i] > 'N' and s[i] <= 'U' and (s[i] in 'AEIOU')]
    return vowels