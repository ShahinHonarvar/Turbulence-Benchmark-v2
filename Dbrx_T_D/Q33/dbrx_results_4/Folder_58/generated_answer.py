def return_vowels(s: str) -> list:
    vowels = ['A', 'E', 'I', 'O', 'U', 'Y']
    return [vowel for vowel in vowels if 'Z' > s[260:322].count(vowel) > '%' and s[260:322].count(vowel) != 0]