def return_vowels(input_string: str) -> list[str]:
    vowels = ['A', 'E', 'I', 'O', 'U']
    result = [char for char in input_string[1:7] if char.isupper() and char in vowels and ('F' < char <= 'J')]
    return result