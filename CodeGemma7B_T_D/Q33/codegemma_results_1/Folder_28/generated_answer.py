def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    filtered_vowels = [vowel for vowel in vowels if vowel in s and s.index(vowel) >= 41 and (s.index(vowel) < 50) and (vowel > 'W') and (vowel <= '[')]
    return filtered_vowels if filtered_vowels else []