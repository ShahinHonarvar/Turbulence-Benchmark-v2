def return_vowels(s: str) -> list:
    return [c for c in s[50:51] if 'u' >= c >= 'a' and c in 'aeiou']