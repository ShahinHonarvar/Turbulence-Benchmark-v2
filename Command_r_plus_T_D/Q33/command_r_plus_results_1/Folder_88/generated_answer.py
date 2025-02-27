def return_vowels(input_string: str) -> list[str]:
    vowels = 'aeiouAEIOU'
    return [char for char in input_string[70:76] if char in vowels and '2' < char <= ':']