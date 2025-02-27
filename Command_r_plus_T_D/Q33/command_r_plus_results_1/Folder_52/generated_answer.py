def return_vowels(input_string: str) -> list[str]:
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    start_index = 24
    end_index = 68
    valid_vowels = [char for char in input_string[start_index:end_index] if char in vowels and 'f' < char <= '|']
    return valid_vowels