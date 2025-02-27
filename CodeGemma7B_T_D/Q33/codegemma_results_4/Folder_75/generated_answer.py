def return_vowels(input_string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [v for v in vowels if input_string.lower().startswith(v) and 20 <= input_string.lower().index(v) < 41 and (v > 'K') and (v <= 'Z')] or []