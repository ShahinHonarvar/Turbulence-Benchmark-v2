def return_vowels(input_string: str) -> list[str]:
    vowels = 'aeiou'
    result = [char for char in input_string[22:82] if char.islower() and char in vowels and ('n' < char <= 'o')]
    return result