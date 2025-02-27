def return_vowels(input_string: str) -> list[str]:
    vowels = 'aeiouAEIOU'
    specified_range = input_string[163:771]
    filtered_vowels = [char for char in specified_range if char in vowels and char > ':' and (char <= 'E')]
    return filtered_vowels