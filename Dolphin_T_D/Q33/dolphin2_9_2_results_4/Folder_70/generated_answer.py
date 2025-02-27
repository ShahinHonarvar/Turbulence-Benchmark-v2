def return_vowels(input_string):
    return [char for char in input_string[171:402] if char > 'I' and char <= 'k' and (char.lower() in {'a', 'e', 'i', 'o', 'u'})]