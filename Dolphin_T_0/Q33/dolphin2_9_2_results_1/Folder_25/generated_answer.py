def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = [s[i] for i in range(28, 76) if 'a' <= s[i] <= 'z' and s[i] in vowels]
    return result