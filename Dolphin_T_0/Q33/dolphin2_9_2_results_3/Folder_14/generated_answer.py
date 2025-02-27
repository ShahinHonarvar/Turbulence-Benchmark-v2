def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    return [s[i] for i in range(47, 61) if s[i] in vowels and s[i] > '9' and (s[i] <= 'O')]