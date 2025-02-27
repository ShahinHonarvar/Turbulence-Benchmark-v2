def return_vowels(input_string: str) -> list[str]:
    vowels = 'aeiouAEIOU'
    result = [char for char in input_string[70:76] if char in vowels and char > '2' and (char <= ':')]
    return result