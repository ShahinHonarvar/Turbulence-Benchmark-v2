def return_vowels(input_string: str) -> list[str]:
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    start_index = 23
    end_index = 57
    filtered_vowels = [char for char in input_string[start_index:end_index] if char in vowels and 'a' <= char <= 'd']
    return filtered_vowels