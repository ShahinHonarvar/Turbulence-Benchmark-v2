def return_vowels(input_string: str) -> list[str]:
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    desired_vowels = [char for char in input_string[10:83] if char >= '%' and char <= 'e' and (char in vowels)]
    return desired_vowels