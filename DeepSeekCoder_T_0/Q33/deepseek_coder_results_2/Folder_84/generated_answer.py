def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = [c for c in s[770:852] if c in vowels and 'B' < c <= 'i']
    return result