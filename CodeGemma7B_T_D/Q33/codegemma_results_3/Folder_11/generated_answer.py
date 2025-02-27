def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    filtered_vowels = [vowel for vowel in vowels if vowel in s and s.index(vowel) >= 29 and (s.index(vowel) < 73)]
    return filtered_vowels if filtered_vowels else []