def return_vowels(parameter):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    return [vowel for vowel in vowels if vowel in parameter and parameter.index(vowel) >= 13 and (parameter.index(vowel) < 37) and (vowel > 'Z') and (vowel <= '}')] or []