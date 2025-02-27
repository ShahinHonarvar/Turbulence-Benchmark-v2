def return_vowels(input_string):
    start_index = 149
    end_index = 313
    vowels = ['a', 'e', 'i', 'o', 'u']
    if len(input_string) < end_index:
        return []
    substring = input_string[start_index:end_index]
    return [char for char in substring if char.lower() > 'm' and char.lower() <= 'j' and (char.lower() in vowels)]