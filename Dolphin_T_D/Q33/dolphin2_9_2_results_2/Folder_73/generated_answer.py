def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [s[i] for i in range(47, 89) if s[i] in vowels and ord('@') < ord(s[i]) <= ord('n')]