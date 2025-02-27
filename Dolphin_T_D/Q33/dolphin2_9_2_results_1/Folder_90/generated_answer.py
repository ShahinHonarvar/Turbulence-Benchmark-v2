def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [s[i] for i in range(142, 145) if s[i] in vowels and ord('a') < ord(s[i]) <= ord('o')]