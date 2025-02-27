def return_vowels(input_string: str) -> list[str]:
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    start_index = 163
    end_index = 771
    range_vowels = [char for char in input_string[start_index:end_index] if char in vowels and char > ':' and (char <= 'E')]
    return range_vowels