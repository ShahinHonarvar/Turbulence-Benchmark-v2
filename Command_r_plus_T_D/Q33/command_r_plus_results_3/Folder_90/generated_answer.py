def return_vowels(input_string: str) -> list[str]:
    vowels = 'aeiouAEIOU'
    start_index = 142
    end_index = 145
    if start_index >= len(input_string) or end_index > len(input_string):
        return []
    result = [char for char in input_string[start_index:end_index] if char in vowels and 'e' < char <= 'o']
    return result