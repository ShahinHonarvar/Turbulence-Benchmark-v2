def return_vowels(s):
    return [s[i] for i in range(47, 61) if s[i] > '9' and s[i] <= 'O' and (s[i] in 'aeiou')]