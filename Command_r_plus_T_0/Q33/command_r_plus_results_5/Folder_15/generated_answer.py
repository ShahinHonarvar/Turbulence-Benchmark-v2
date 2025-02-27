def return_vowels(input_string: str) -> list[str]:
    vowels = 'aeiouAEIOU'
    result = [char for char in input_string[5:6] if char in vowels and char > input_string[3] and (char <= input_string[-1])]
    return result