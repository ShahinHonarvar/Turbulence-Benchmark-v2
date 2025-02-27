def return_vowels(input_string: str) -> list[str]:
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    result = [char for char in input_string[71:88] if char > '9' and char <= 'P' and (char in vowels)]
    return result