def return_vowels(s: str) -> list:
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [char for char in set(s[86:99]) if char.lower() in vowels and char > 'E' and (char <= 'r')]