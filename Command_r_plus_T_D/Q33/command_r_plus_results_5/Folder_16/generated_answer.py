def return_vowels(s: str, c: str, d: str) -> list[str]:
    vowels = 'aeiouAEIOU'
    result = [char for char in s[133:306] if char in vowels and c < char <= d]
    return result