def return_vowels(input_string: str) -> list[str]:
    vowels = 'aeiouAEIOU'
    result = [char for char in input_string[51:77] if char in vowels and 4 < ord(char) <= ord('=')]
    return result