def return_vowels(input_string: str, c: str, d: str) -> list[str]:
    vowels = 'aeiouAEIOU'
    return [char for char in input_string[134:306] if char in vowels and c < char <= d]