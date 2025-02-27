def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = [s[i] for i in range(1, 4) if s[i] in vowels and 'c' < s[i] <= 'i']
    return result