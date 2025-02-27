def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = [c for c in s[27:57] if c in vowels and 'o' < c <= 'w']
    return result