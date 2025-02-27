def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = [s[i] for i in range(s.index('@') + 1, s.index('n') + 1) if i in range(47, 89) and s[i] in vowels]
    return result