def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = [s[i] for i in range(13, 37) if s[i] in vowels and 'Z' < s[i] <= '}']
    return result