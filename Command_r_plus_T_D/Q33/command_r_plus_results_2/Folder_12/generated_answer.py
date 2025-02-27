def return_vowels(input_string: str) -> list[str]:
    vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
    start_index = 13
    end_index = 37
    result = []
    for index in range(start_index, end_index):
        char = input_string[index]
        if char > 'Z' and char <= '}' and (char in vowels):
            result.append(char)
    return result