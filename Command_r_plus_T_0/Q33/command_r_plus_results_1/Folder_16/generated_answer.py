def return_vowels(input_string: str, c: str, d: str) -> list[str]:
    vowels = 'aeiouAEIOU'
    result = [char for char in input_string[133:306] if char in vowels and c < char <= d]
    return result