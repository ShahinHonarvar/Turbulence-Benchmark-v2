def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = [s[i] for i in range(46, 49) if s[i] in vowels and '\\' < s[i] <= 'p']
    return result