def return_vowels(input_string: str) -> list[str]:
    vowels = 'aeiouAEIOU'
    result = [char for char in input_string[5:6] if char in vowels and 3 < ord(char) <= ord(input_string[-1])]
    return result