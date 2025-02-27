def return_vowels(s: str) -> list[str]:
    vowels = ['a', 'e', 'i', 'o', 'u']
    filtered_vowels = [vowel for vowel in vowels if vowel in s and vowels.index(vowel) >= 21 and (vowels.index(vowel) <= 59) and (vowel > '/') and (vowel <= 'a')]
    return filtered_vowels