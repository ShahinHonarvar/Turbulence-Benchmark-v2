def return_vowels(s: str) -> list:
    vowels = [c for c in s[21:59] if 'a' >= c > '/']
    return sorted(list(set(vowels)))