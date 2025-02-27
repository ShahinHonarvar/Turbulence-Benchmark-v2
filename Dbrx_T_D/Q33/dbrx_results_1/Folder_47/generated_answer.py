def return_vowels(s: str) -> list:
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [char for char in s[23:38] if s.index(char) > 22 and s.index(char) < 38 and (vowels.count(char.lower()) > 0) and ('N' < char <= 'k')]