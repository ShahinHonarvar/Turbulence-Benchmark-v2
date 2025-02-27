def return_vowels(input_string: str) -> list[str]:
    vowels = 'aeiouAEIOU'
    return [char for char in input_string[202:872] if char in vowels and 3 < ord(char) <= ord('>')]