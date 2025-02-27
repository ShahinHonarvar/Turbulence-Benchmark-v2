def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = [s[i] for i in range(34, 58) if s[i] in vowels and s[i] > 'b' and (s[i] <= 'o')]
    return result