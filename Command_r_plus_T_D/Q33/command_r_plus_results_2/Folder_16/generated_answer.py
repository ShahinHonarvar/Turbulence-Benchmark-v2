def return_vowels(s: str, c: str, d: str) -> list[str]:
    vowels = 'aeiouAEIOU'
    result = [vowel for vowel in s[133:306] if vowel in vowels and c < vowel <= d]
    return result