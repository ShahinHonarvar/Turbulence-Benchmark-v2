def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = [s[i] for i in range(14, 60) if s[i] in vowels and s[i] > 'D' and (s[i] <= 'v')]
    return result