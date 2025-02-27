def return_vowels(s: str) -> list:
    vowels = ['A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u']
    result = [char for char in s[495:837] if char > 'B' and char <= 't' and (char in vowels)]
    return result