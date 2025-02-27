def return_vowels(input_string):
    if len(input_string) > 8:
        return [char for char in input_string[8:9] if char in 'aeiouAEIOU' and 'Y' < char <= 's']
    return []