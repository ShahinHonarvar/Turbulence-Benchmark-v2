def return_vowels(input_string: str) -> list[str]:
    vowels = 'aeiouAEIOU'
    result = [char for char in input_string[13:35] if char > '8' and char <= 'F' and (char in vowels)]
    return result