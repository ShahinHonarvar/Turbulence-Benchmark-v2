def return_vowels(s: str) -> list:
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [char for char in s[171:402] if char > 'i' and char <= 'k' and (char in vowels)]