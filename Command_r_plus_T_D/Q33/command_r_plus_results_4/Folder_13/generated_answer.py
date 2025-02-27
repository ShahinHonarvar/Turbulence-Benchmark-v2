def return_vowels(input_string: str) -> list[str]:
    vowels = 'aeiouAEIOU'
    desired_range = input_string[149:313]
    result = [char for char in desired_range if char in vowels and 'M' < char <= 'j']
    return result