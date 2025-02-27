def return_vowels(input_string: str) -> list[str]:
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    desired_range = input_string[11:53]
    result = [char for char in desired_range if char in vowels and '+' < char <= 'W']
    return result