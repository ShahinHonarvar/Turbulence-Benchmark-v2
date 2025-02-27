def return_vowels(input_string: str) -> list[str]:
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [char for char in input_string[3:9] if char.lower() in vowels and 's' < char.lower() <= 'u']