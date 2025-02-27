def return_vowels(input_string: str) -> list[str]:
    vowels = 'aeiouAEIOU'
    result = [char for char in input_string[40:94] if char in vowels and ord(char) > 4 and (ord(char) <= ord('H'))]
    return result