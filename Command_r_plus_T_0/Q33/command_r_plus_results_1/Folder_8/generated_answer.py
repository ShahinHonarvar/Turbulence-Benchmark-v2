def return_vowels(input_string: str) -> list[str]:
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = [char for char in input_string[64:82] if char.islower() and char > 'p' and (char <= 'z') and (char in vowels)]
    return result