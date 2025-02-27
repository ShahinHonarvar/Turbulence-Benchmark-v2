def return_vowels(s: str) -> list:
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [char for char in s[70:76] if char > '2' and char <= ':' and (char in vowels)]