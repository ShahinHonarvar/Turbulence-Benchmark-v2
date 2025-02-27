def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = [s[i] for i in range(71, 81) if s[i] in vowels and s[i] > '>' and (s[i] <= 'U')]
    return result if result else []