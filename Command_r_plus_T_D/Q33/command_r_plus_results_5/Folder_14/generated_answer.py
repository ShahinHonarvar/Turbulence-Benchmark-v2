def return_vowels(input_string: str) -> list[str]:
    vowels = 'aeiouAEIOU'
    return [char for char in input_string[47:61] if char in vowels and 9 < ord(char) <= ord('O')]