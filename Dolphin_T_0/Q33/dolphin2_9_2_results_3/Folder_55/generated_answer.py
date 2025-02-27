def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = [s[i] for i in range(1, 5) if s[i] in vowels and s[i] > '!' and (s[i] <= 'j')]
    return result