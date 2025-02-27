def return_vowels(s: str) -> list:
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [char for char in s[10:82] if char in vowels and s[9] > '$' and (s[9] <= '@') and (s[81] > '$') and (s[81] <= '@')]