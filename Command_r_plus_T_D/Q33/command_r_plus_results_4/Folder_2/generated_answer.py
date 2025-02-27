def return_vowels(input_string: str) -> list[str]:
    vowels = 'aeiouAEIOU'
    result = [char for char in input_string[170:645] if char in vowels and 'E' < char <= '~']
    return result