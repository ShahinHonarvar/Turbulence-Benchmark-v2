def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    chars = [s[i] for i in range(2, 7) if s[i] > '^' and s[i] <= 'd' and (s[i] in vowels)]
    return chars