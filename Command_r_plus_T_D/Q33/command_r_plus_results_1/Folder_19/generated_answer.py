def return_vowels(input_string: str) -> list[str]:
    vowels = 'aeiouAEIOU'
    specified_range = input_string[51:77]
    filtered_vowels = [char for char in specified_range if char in vowels and char > '4' and (char <= '=')]
    return filtered_vowels