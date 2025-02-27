def return_vowels(input_string: str) -> list[str]:
    vowels = 'aeiouAEIOU'
    desired_range = input_string[13:35]
    result = [char for char in desired_range if char in vowels and 8 < ord(char) <= 70]
    return result