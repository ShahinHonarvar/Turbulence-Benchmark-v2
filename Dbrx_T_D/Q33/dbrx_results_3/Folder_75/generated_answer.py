def return_vowels(input_string):
    vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
    result_list = [char for char in input_string[20:41] if char > 'K' and char <= 'Z' and (char in vowels)]
    return result_list