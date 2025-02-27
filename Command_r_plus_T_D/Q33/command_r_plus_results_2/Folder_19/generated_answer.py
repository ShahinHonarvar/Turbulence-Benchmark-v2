def return_vowels(input_string: str) -> list[str]:
    vowels = 'aeiouAEIOU'
    return [char for char in input_string[51:77] if char in vowels and char > '4' and (char <= '=')]