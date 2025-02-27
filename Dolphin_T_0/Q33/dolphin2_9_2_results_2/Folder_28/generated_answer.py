def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [vowel for vowel in s[41:50] if vowel > 'W' and vowel <= '[' and (vowel in vowels)]