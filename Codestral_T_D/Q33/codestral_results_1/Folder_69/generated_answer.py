def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [s[i] for i in range(641, 872) if s[i] in vowels and '>' < s[i] <= 'q']