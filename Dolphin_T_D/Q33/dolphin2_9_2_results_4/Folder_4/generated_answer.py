def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [s[i] for i in range(40, 91) if s[i] in vowels and 'a' < s[i] <= 'x']