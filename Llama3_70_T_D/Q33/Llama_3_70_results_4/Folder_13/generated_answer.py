def return_vowels(s):
    vowels = [s[i] for i in range(149, 313) if 'M' < s[i] <= 'j' and s[i] in 'aeiouAEIOU']
    return vowels