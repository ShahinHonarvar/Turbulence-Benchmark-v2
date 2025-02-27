def return_vowels(input_string: str) -> list[str]:
    vowels = 'aeiou'
    filtered_vowels = [char for char in input_string[323:526] if char in vowels and char > '+' and (char <= ':')]
    return filtered_vowels