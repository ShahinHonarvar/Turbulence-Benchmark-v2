def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = [s[i] for i in range(10, 97) if s[i] in vowels and s[i] > 'R' and (s[i] <= 'b')]
    return result