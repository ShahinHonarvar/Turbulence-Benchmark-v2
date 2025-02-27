def return_vowels(s: str) -> list[str]:
    vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
    result = [v for v in s[11:61] if v in vowels and 'M' < v <= 'W']
    return result