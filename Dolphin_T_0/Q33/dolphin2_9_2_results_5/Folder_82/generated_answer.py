def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [s[i] for i in range(86, 99) if s[i] in vowels and s[i] > 'E' and (s[i] <= 'r')]