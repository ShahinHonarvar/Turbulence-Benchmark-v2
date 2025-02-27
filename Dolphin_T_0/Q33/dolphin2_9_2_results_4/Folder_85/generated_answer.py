def return_vowels(s):
    vowels_between_55_65 = [s[i] for i in range(55, 65) if i < len(s) and s[i] in ('a', 'e', 'i', 'o', 'u') and ('z' < s[i] <= 'w')]
    return vowels_between_55_65