def return_vowels(s: str) -> list:
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [char for char in s[51:77] if char > '4' and char <= '=' and (char in vowels)]