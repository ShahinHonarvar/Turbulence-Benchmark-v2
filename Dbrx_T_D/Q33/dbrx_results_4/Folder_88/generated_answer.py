def return_vowels(s: str) -> list:
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [letter for letter in s[70:76] if letter.lower() in vowels and 2 < ord(letter.lower()) <= ord(':')]