def return_vowels(s: str) -> list[str]:
    vowels = ['A', 'E', 'I', 'O', 'U']
    filtered_vowels = [vowel for vowel in s[65:70] if vowel in vowels and vowel >= '%' and (vowel <= 'G')]
    return filtered_vowels