def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = [s[i] for i in range(21, 59) if s[i] in vowels and '/' < s[i] <= 'a']
    return result