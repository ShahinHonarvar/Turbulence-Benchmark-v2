def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = [s[i] for i in range(21, 23) if s[i] in vowels and 'm' <= s[i] <= 'n']
    return result