def return_vowels(input_string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    character_range = input_string[29:73]
    result = [ch for ch in character_range if ch > ' ' and ch <= '.' and (ch.lower() in vowels)]
    return result