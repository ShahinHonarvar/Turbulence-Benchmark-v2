def return_vowels(s: str) -> list[str]:
    vowels = 'aeiouAEIOU'
    start, end = (51, 77)
    result = [char for char in s[start:end] if char in vowels and char > '4' and (char <= '=')]
    return result