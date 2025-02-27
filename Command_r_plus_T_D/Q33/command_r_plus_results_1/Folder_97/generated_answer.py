def return_vowels(input_string: str) -> list[str]:
    vowels = 'aeiouAEIOU'
    result = [char for char in input_string[328:455] if char in vowels and '>' < char <= 'z']
    return result