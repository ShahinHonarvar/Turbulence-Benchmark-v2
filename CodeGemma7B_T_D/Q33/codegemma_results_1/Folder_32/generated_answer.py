from typing import List

def return_vowels(text: str) -> List[str]:
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [vowel for vowel in vowels if vowel in text[45:76] and vowel > 'b' and (vowel <= 'z')]