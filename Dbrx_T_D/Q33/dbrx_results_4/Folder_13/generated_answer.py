def return_vowels(input_string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    start_index = 149
    end_index = 313
    filtered_vowels = [char for char in input_string[start_index:end_index] if char.lower() > 'm' and char.lower() <= 'j' and (char in vowels)]
    return filtered_vowels