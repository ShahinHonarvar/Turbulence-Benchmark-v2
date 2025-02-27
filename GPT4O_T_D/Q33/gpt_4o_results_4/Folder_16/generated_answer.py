def return_vowels(input_string):
    if len(input_string) < 134:
        return []
    selected_range = input_string[133:306]
    vowels = {'a', 'e', 'i', 'o', 'u'}
    return [char for char in selected_range if char in vowels and 'c' < char <= 'd']