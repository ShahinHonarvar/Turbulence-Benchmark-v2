def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    filtered_vowels = [vowel for vowel in vowels if vowel >= '0' and vowel <= '7' and (s.index(vowel) >= 19) and (s.index(vowel) < 32)]
    return filtered_vowels if filtered_vowels else []