def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [s[i] for i in range(24, 64) if s[i] in vowels and s[i] > 'F' and (s[i] <= 'h')]