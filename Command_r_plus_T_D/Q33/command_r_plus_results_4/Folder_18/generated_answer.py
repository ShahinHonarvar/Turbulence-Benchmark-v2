def return_vowels(input_string: str) -> list[str]:
    vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
    desired_range = input_string[528:606]
    result = [char for char in desired_range if char in vowels and 'M' < char <= 'X']
    return result