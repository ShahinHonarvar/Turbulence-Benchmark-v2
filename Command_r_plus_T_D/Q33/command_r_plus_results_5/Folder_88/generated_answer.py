def return_vowels(input_string: str) -> list[str]:
    vowels = 'aeiouAEIOU'
    start_index = 70
    end_index = 76
    result = []
    for char in input_string[start_index:end_index]:
        if char in vowels and '2' < char <= ':':
            result.append(char)
    return result