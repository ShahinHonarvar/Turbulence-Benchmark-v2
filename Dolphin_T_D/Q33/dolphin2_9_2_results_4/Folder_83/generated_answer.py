def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = [s[i] for i in range(90, 97) if s[i] in vowels and s[i] > '_' and (s[i] <= 'x')]
    return result