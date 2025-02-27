def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = [vowel for vowel in s[90:97] if vowels.index(vowel) >= 2 and vowels.index(vowel) < 5]
    return result