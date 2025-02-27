def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    return [s[i] for i in range(17, 65) if s[i] in vowels and s[i] > 'U' and (s[i] <= '{')]