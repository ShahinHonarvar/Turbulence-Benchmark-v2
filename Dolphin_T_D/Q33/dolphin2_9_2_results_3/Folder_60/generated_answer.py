def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = [s[i] for i in range(24, 59) if s[i] in vowels and s[i] > 'n' and (s[i] <= 'u')]
    return result