def return_vowels(s: str) -> list:
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [char for char in s[29:73] if char > '#' and char <= '(' and (char in vowels)]