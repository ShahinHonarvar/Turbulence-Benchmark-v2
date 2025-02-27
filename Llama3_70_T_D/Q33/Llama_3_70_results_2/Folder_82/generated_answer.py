def return_vowels(s):
    vowels = [s[i] for i in range(86, 99) if 'E' < s[i] <= 'r' and s[i] in 'aeiou']
    return vowels